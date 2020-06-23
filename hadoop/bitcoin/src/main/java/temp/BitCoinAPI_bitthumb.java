package temp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class BitCoinAPI_bitthumb extends Thread {

	//bitthumb menu
	static String[] subMenu = {"opening_price","closing_price","min_price","max_price","average_price","units_traded","volume_1day","volume_7day","buy_price","sell_price","24H_fluctate","24H_fluctate_rate"};
	static String[] coinMenu = {"BTC","ETH","DASH","LTC","ETC","XRP","BCH","XMR","ZEC","QTUM","BTG","EOS","ICX","VET","TRX","ELF","MITH","MCO","OMG","KNC","GNT","HSR","ZIL","ETHOS","PAY","WAX","POWR","LRC","GTO","STEEM","STRAT","ZRX","REP","AE","XEM","SNT","ADA","PPT","CTXC","CMT","THETA","WTC","ITC","TRUE","ABT","RNT","PLY","WAVES","LINK","ENJ","PST"};
	static String fileName = "/home/hadoop/source_data/bitthumbitCoin/bitthumbitCoin";
	static String fileCount = "/home/hadoop/crawler/bitThumb_fileCount.txt";
	static String realFileSuffix = ".csv.tmp";
	static String completeFileSuffix = ".csv";
	
	public void run(){
		
		System.out.println("## BitCoinAPI_bitthumb Call Start !! ##");
		
		BufferedReader rd = null;
		BufferedWriter bw = null;
		String line = "";
		String result = "";
		HttpsURLConnection huc = null;
		
		//bitthumb Header
		// CoinCode , opening_price,closing_price,min_price,max_price,average_price,units_traded,volume_1day,volume_7day,buy_price,sell_price,24H_fluctate,24H_fluctate_rate,day_time
		
		try {
			String filePath = getFilePath(fileName);
			//Coinone Api Call
			//URL url = new URL("https://api.coinone.co.kr/ticker/?currency=all&format=json");
			//Coinnest Api Call
			//URL url = new URL("https://api.coinnest.co.kr/api/pub/tickerall");
			
			//BitThumb Api Call
			URL url = new URL("https://api.bithumb.com/public/ticker/ALL");
			
			huc = (HttpsURLConnection)url.openConnection();
			huc.addRequestProperty("user-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0");
			huc.setRequestMethod("GET");
			
			rd = new BufferedReader(new InputStreamReader(huc.getInputStream(),"UTF-8"));
			bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath, true), "UTF-8"));		
			
			// bithumb 사이트에 연결하여 읽은 데이타을 한 줄 씩 읽어서 result 변수에 추가한다
			while ((line = rd.readLine()) != null) {
				 result += line+"\n";
			}
			
			// 저장한 데이타를 json으로 변환하고 csv 파일로 저장한다
			if(result.length() != 0){
				 JsonObject json = jsonTransper(result);
				 jsonToCSV(json,bw);
			}else {
				 System.out.println("Text Data--length 0");
			}
			
			rd.close(); 
			bw.close();			 
			 
		} catch (Exception e) {
			System.out.println("[ 연결하여 데이타를 읽고 저장시 오류 ] ");
			e.printStackTrace();
		}
		
		
	}
	
	/**
		문자열을 JSON 구조로 변환하는 함수
	 */
	private static JsonObject jsonTransper(String jsonText){
		
		JsonParser parser = new JsonParser();
		JsonObject json = new JsonObject();
		
		try {		
			JsonElement je = parser.parse(jsonText);		// 문자열을 json 구조로 변경
			json = je.getAsJsonObject().getAsJsonObject("data"); // json 구조를 JSON 객체로 변경
			
		} catch (Exception e) {
			System.out.println("[ 문자열로 받은 데이타를 JSON 구조로 변경시 오류  ]");
			e.printStackTrace();
		}	
		
		return json;
	}
	
	
	/**
		JSON 데이타를 CSV 파일로 저장
	 */
	private static String jsonToCSV (JsonObject json, BufferedWriter bw){
			
			String csv = "";
			
			try {
			
				for (int i = 0; i < coinMenu.length; i++) {
					
					csv = coinMenu[i]+",";
					
					// 코인 메뉴의 값이 없으면 continue 한다는 것은
					// 값이 있으면 아래 반복문에서 그 값들을 전공한다.
					if(json.getAsJsonObject(coinMenu[i]) == null ) continue;
					
					for (int j = 0; j < subMenu.length; j++) {
						// 코인메뉴의 값들을 지정된 파일에 저장한다
						csv += json.getAsJsonObject(coinMenu[i]).get(subMenu[j])+",";
						if(j == subMenu.length-1){
							csv += json.get("date");
							System.out.println(json.get("date"));
							bw.write(csv);
							bw.newLine();							
						}
						
					}
				}
				
			} catch (Exception e) {
				System.out.println("[ JSON 객체를 csv 파일로 저장시 오류 ]");
				e.printStackTrace();
			}		
			
			return csv;
		}
	
	
	/**
		tmp 파일을 csv 파일로 변경하고  파일 갯수를 저장하는 함수
	 */
	public static String getFilePath(String s){
		String realFilePath = "";
		String completeFilePath = "";
		

		BufferedWriter bw = null;
		
		try {
			// 파일 갯수를 저장하는 /home/hadoop/crawler/bitThumb_fileCount.txt 파일에서
			// 파일 갯수을 읽어서 fileNumber 변수에 저장한다
			FileReader fr = new FileReader(fileCount);
			BufferedReader br = new BufferedReader(fr);
			int fileNumber = Integer.parseInt(br.readLine());
			br.close();
			
			// realFilePath = "/home/hadoop/source_data/bitthumbitCoin/bitthumbitCoin" + 파일수 + ".csv.tmp"
			// completeFilePath = "/home/hadoop/source_data/bitthumbitCoin/bitthumbitCoin" + 파일수 + ".csv"
			realFilePath = s+fileNumber+realFileSuffix;
			completeFilePath = s+fileNumber+completeFileSuffix;
			
			File realFile = new File(realFilePath);
			File completeFile = new File(completeFilePath);

			// tmp 파일이 존재하고 해당 파일의 길이가 131072(2의 몇 승?)
			// tmp 파일을 csv 파일로 이름을 변경하고 다시 파일 수를 증가하고 파일수를 저장한다
			if(realFile.exists() && realFile.length() > 131072){
				realFile.renameTo(completeFile);
				
				fileNumber++;
				realFilePath = s+fileNumber+realFileSuffix;
				
				// 파일 갯수를 저장하는 /home/hadoop/crawler/bitThumb_fileCount.txt 파일에 파일 갯수 저장
				bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(fileCount)));
				bw.write(String.valueOf(fileNumber));
				bw.close();
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		return realFilePath;		
	}
	
}
