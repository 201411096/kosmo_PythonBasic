package sample2;

import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;


public class TopNMain {

	public static class WordFreqComparator implements Comparator<WordFreq>{		
		// 2개의 WordFreq를 비교하여 결과값 리턴 
		public int compare(WordFreq a, WordFreq b){
			if(a.getFreq() < b.getFreq()){	return -1;	}			
			if(a.getFreq() > b.getFreq()){	return 1;	}			
			return 0;			
		}
	}
	
	// Mapper class
	public static class Map extends Mapper<Text, Text, Text, LongWritable>{
		
		int topN= 10;
		
		Comparator<WordFreq> comparator = new WordFreqComparator();
		PriorityQueue<WordFreq> queue = new PriorityQueue<WordFreq>(topN, comparator);
				
		protected void setup(Context context) throws IOException, InterruptedException{
			topN=context.getConfiguration().getInt("topN",topN);
			// 환경변수에 "topN"이 없다면 두번째 지정한  int 값을 디폴트값으로 지정한다.
			// [참고] https://hadoop.apache.org/docs/r2.4.1/api/org/apache/hadoop/conf/Configuration.html		
		}
		
		//  map : 입력되는 레코드가 있을 때마다 반복적으로 수행되는 메소드 
		public void map(Text key, Text value, Context context) throws IOException, InterruptedException{
			Long lValue = Long.parseLong(value.toString()); // 빈도수를 숫자형으
			
			insert(queue, key.toString(), lValue, topN);
		}
		
		// map() 메소드가 모두 호출된 후에 cleanup() 메소드 호출
		// 모든 입력 레코드가 완료되었을 때 잡 요청을 한다. ( context.write() )
		protected void cleanup(Context context) throws IOException, InterruptedException{
			while (queue.size() !=0){
				WordFreq wordF = (WordFreq)queue.remove(); // 빈도수가 작은 것부터 나온다 
				// context.write(Text, LongWritable) // 출력형식 맞추기  
				context.write(new Text(wordF.getWord()),new LongWritable(wordF.getFreq()));
			}
		}
	}
	
	// Reducer class
	//    리듀스의 입력형식  :  Text,LongWritable  (** 맵의 출력형식과 일치 )
	//    리듀스의 출력형식 :   Text,LongWritable 
	public static class Reduce extends Reducer<Text,LongWritable, Text, LongWritable>{
		int topN=10;
		Comparator<WordFreq> comparator = new WordFreqComparator();
		PriorityQueue<WordFreq> queue = new PriorityQueue<WordFreq>(topN, comparator);
			
		protected void setup(Context context) throws IOException, InterruptedException{
			topN=context.getConfiguration().getInt("topN", topN);
		}
		
		// 각 맵들에서 추출한 N개의 받아서 이 중에서 다시 N개를 추출한다. 
		public void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException{
			long sum = 0;
			for(LongWritable val : values){
				// 값이 1개만 들어 있다 하더라도 List 형식이기에 반복문 
				sum +=val.get();
			}			
			insert(queue, key.toString(), sum, topN);
		}
		
		protected void cleanup(Context context) throws IOException, InterruptedException{
			while(queue.size() !=0){
				WordFreq wordF = (WordFreq)queue.remove();
				// context.write(Text, LongWritable) // 출력형식 맞추기  
				context.write(new Text(wordF.getWord()), new LongWritable(wordF.getFreq()));
			}
		}
	}
	

	// 인자 : 우선순위큐, 단어, 빈도수, 상위N개 
	//  N값 -  큐의 갯수 
	public static void insert(PriorityQueue queue, String word, Long lValue, int topN){
		
		WordFreq miniWF = (WordFreq)queue.peek();
		// 우선순위큐는 지정한 준에 (빈도수)따라 순서대로 저장하고 있기에 
		//peek() 호출시 빈도수가 작은 (즉, 우선순위가 낮은) 원소가 출력된다. 
		
		// 큐의 갯수가  N개보다 작으면 큐에 추가
		// 큐의 갯수보다 큰 경우에서는 큐에서 우선순위가 낮은 원소의 빈도수보다 크면 큐에 추가 
		if(queue.size() < topN || miniWF.getFreq() < lValue ){
			WordFreq wordFreq = new WordFreq(word, lValue);
			queue.add(wordFreq);
		}		
		// 조건에 맞아서 큐에 넣은 경우  큐의 크기가 10개를 넘으면 
		// 우선순위 낮은 원소 삭제하여 큐의 갯수를 10개 유지한다.
		if(queue.size() > topN){
			queue.remove();
		}
	}		
	
	
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "TopNMain");
		
		job.setJarByClass(TopNMain.class);
		job.setMapperClass(Map.class);
		job.setReducerClass(Reduce.class);
		job.setNumReduceTasks(1); // 리듀스태스크 1개로 지정 		

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(LongWritable.class);			
		
		job.setInputFormatClass(KeyValueTextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		job.getConfiguration().setInt("topN", Integer.parseInt(args[2]));
		// 잡의 설정값 추가하여 Map과 Reduce 클래스에서 사용가능 
		
		job.waitForCompletion(true);
	}
}

