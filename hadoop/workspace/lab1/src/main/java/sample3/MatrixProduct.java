package sample3;

import java.io.IOException;
import java.util.HashMap;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
 
public class MatrixProduct {
 
    public static class Map extends Mapper<LongWritable, Text, Text, Text> {
        public void map(LongWritable key, Text value, Context context)
          throws IOException, InterruptedException {
            Configuration conf = context.getConfiguration();
            //행렬 A와 B의 크기를 정의한다.
            int m = Integer.parseInt(conf.get("m"));
            int n = Integer.parseInt(conf.get("n"));
            int p = Integer.parseInt(conf.get("p"));
 
            String line = value.toString();
            String[] indicesAndValue = line.split(",");
            Text outputKey = new Text();
            //Key와 Value를 저장할 값을 정의한다.
            Text outputValue = new Text();
            //Split의 각 줄을 , 단위로 나눈다.
 
            //Key는 행렬곱의 결과로 출력되는 행렬의 위치이다.
            //Value는 해당 행렬의 이름과 위치, 값을 정의한다.
            if (indicesAndValue[0].equals("A")) {
                for (int k = 0; k < p; k++) {
                    outputKey.set(indicesAndValue[1] + "," + k);
                    outputValue.set("A," + indicesAndValue[2] + "," + indicesAndValue[3]);
                    context.write(outputKey, outputValue);
                }
            } else {
                for (int i = 0; i < m; i++) {
                    outputKey.set(i + "," + indicesAndValue[2]);
                    outputValue.set("B," + indicesAndValue[1] + "," + indicesAndValue[3]);
                    context.write(outputKey, outputValue);
                }
            }
        }
    }
 
    public static class Reduce extends Reducer<Text, Text, Text, Text> {
        public void reduce(Text key, Iterable<Text> values, Context context)
          throws IOException, InterruptedException {
            Configuration conf = context.getConfiguration();
 
            //각 행렬의 위치와 값을 저장할 수 있는 Map을 생성한다.
            HashMap<Integer, Double> hashA = new HashMap<Integer, Double>();
            HashMap<Integer, Double> hashB = new HashMap<Integer, Double>();
            for (Text val : values) {
            	String[] value = val.toString().split(",");
                if (value[0].equals("A")) {
                    hashA.put(Integer.parseInt(value[1]), Double.parseDouble(value[2]));
                } else {
                    hashB.put(Integer.parseInt(value[1]), Double.parseDouble(value[2]));
                }
            }
            //행렬 A와 B의 크기를 정의한다.
            int m = Integer.parseInt(conf.get("m"));
            int n = Integer.parseInt(conf.get("n"));
            int p = Integer.parseInt(conf.get("p"));
 
            double result = 0.0;
 
            //각 행렬의 요소들과 비교하여 일치하면 서로 곱한 후 더한다.   
            for (int j = 0; j < n; j++) {
                double a_ij = hashA.containsKey(j) ? hashA.get(j) : 0.0;
                double b_jk = hashB.containsKey(j) ? hashB.get(j) : 0.0;
                result += a_ij * b_jk;
            }
            if (result != 0.0f) {
                context.write( key, new Text(""+result) );
            }
        }
    }
 
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        //행렬의 크기를 설정해줍니다.
        // 첫번째 행렬  m * n
        // 두번째 행렬  n * p
        conf.set("m", "2");  
        conf.set("n", "5"); 
        conf.set("p", "3");
 
        //Job job = new Job(conf, "MatrixMultiplication");
        Job job = Job.getInstance(conf, "MatrixMultiplication");
        // 각 클래스 지정
        job.setJarByClass(MatrixProduct.class);       
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);
        
        // 출력 Key, Value타입 지정
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
 
        // 입력포맷과 출력포맷 지정
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
 
        // 파일입력포맷와 파일출력포맷 지정
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
 
        //하둡 분산 프로그램을 실행한다.
        job.waitForCompletion(true);
    }
}
