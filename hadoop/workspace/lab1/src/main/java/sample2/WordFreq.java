package sample2;

/**
 * 입력되는 레코드을 저장하는 클래스 
 */
public class WordFreq {
	// 단어, 빈도
	private String word;
	private Long freq;
	
	// 생성
	public WordFreq(){
		this.word="";
		this.freq=0L;
	}
	
	public WordFreq(String word, long freq){
		this.word=word;
		this.freq=freq;
	}
	
	//setter, getter
	public String getWord(){
		return word;
	}
	
	public void setWord(String word){
		this.word=word;
	}
	//setter, getter
	public Long getFreq(){
		return freq;
	}
	
	public void setFreq(Long freq){
		this.freq=freq;
	}
}
