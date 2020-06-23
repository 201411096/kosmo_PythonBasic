package temp;

public class MainApp 
{
    public static void main( String[] args )
    {
        
    	try {
			
    		BitCoinAPI_bitthumb bitThumb = null;
        	//BitCoinAPI_coinone coinOne = null;
        	//BitCoinAPI_upbit upbit = null;
        	
        	int count = 0;
        	
        	/** 지속적인 데이타를 받으려고 일부러 쓰레드 구동하고  그냥  카운트 확인 하는 것임 ( 특별한 이유가 없음 ) */
        	while (true) {        		
        		Thread.sleep(1000);
        		System.out.println("Time Count == "+ count +"seconds");
        		if(count%10 == 0){
        			bitThumb = new BitCoinAPI_bitthumb();
        			//coinOne = new BitCoinAPI_coinone();
        			//upbit = new BitCoinAPI_upbit();
        			
        			bitThumb.start();
                	//coinOne.start();
                	//upbit.start();		
        		}
        		count++;
        	}
    		
		} catch (Exception e) {
			System.out.println("##### Process End #####");
			e.printStackTrace();
		}
    	
    }
}
