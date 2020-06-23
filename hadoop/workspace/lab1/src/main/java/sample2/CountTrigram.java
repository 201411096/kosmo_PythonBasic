package sample2;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class CountTrigram {

	public static class Map extends Mapper<Text, Text, Text, IntWritable>{
		private final static IntWritable one = new IntWritable(1);
		private Text trigram = new Text();
		
		// A B C D E --> (A B C), (B C D), (C D E) 추출후에 다시 
		// B C D E F 에서  3개씩  묶는다 
		public void map(Text key, Text value, Context context) throws IOException, InterruptedException{
			String line = value.toString();
			
			StringTokenizer tokenizer = new StringTokenizer(line,"\t\r\n\f |,!#\"$.'%&=+-_^@`~:?<>(){}[];*/");
			if(tokenizer.countTokens() >= 3){
				String firstToken = tokenizer.nextToken().toLowerCase();
				String secondToken = tokenizer.nextToken().toLowerCase();
				
				while(tokenizer.hasMoreTokens()){
					String thirdToken = tokenizer.nextToken().toLowerCase();
					trigram.set(firstToken+" "+secondToken+" "+thirdToken);
					context.write(trigram, one);
					
					firstToken = secondToken;
					secondToken = thirdToken;
				}
			}
		}
	}
	
	
	// 리듀서 클래스 
	public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable>{
		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException{
			int sum = 0;
			for (IntWritable val : values){
				sum +=val.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}
	
	// 잡을 2개를 생성 - CountTrigram / TopNMain
	public static void main(String[] args) throws Exception {
		Configuration conf1 = new Configuration();
		Job job1 = Job.getInstance(conf1, "Count Trigram");
		
		job1.setJarByClass(CountTrigram.class);
		job1.setMapperClass(Map.class);
		job1.setCombinerClass(Reduce.class);
		job1.setReducerClass(Reduce.class);

		job1.setOutputKeyClass(Text.class);
		job1.setOutputValueClass(IntWritable.class); //***
		
		job1.setInputFormatClass(KeyValueTextInputFormat.class);
		job1.setOutputFormatClass(TextOutputFormat.class);
		
		FileInputFormat.addInputPath(job1, new Path(args[0]));
		FileOutputFormat.setOutputPath(job1, new Path(args[1]));

		if(!job1.waitForCompletion(true)) return;
		
		//--------------------------------------------------
		Configuration conf2 = new Configuration();
		Job job2 = Job.getInstance(conf2, "TopNMain");
		
		job2.setJarByClass(TopNMain.class);
		job2.setMapperClass(TopNMain.Map.class); 	 //# 클래스 
		job2.setReducerClass(TopNMain.Reduce.class); //# 클래스 
		job2.setNumReduceTasks(1);

		job2.setOutputKeyClass(Text.class);
		job2.setOutputValueClass(LongWritable.class);
		
		job2.setInputFormatClass(KeyValueTextInputFormat.class);
		job2.setOutputFormatClass(TextOutputFormat.class);
		
		// 위의 잡에서 출력된 내용을 입력으로 받아야 함 
		// 출력경로 :  입력경로 / topN 하위폴더 
		FileInputFormat.addInputPath(job2, new Path(args[1]));
		FileOutputFormat.setOutputPath(job2, new Path(args[1]+"//topN"));
		job2.getConfiguration().setInt("topN", 10);
		
		if(!job2.waitForCompletion(true)) return;
	}


}
