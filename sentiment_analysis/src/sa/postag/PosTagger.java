package sa.postag;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;

import opennlp.tools.postag.POSModel;
import opennlp.tools.postag.POSTaggerME;

public class PosTagger {

	public PosTagger(String INPUT_FILE, String OUTPUT_FILE){
		
	    FileWriter fstream;
	    BufferedWriter out;
	    String line_out = "";   
	    
	    try {
	    
		    fstream = new FileWriter(OUTPUT_FILE);
	        out = new BufferedWriter(fstream);
	                
	        BufferedReader in = new BufferedReader(new FileReader(INPUT_FILE));
	        String line_input = "";
	        		
	        while (true) {
	        	line_input = in.readLine();
	        	
	        	line_out = getRelevantPos(line_input.split(" "));
                
	        	System.out.println(line_input);
	        	System.out.println(line_out);
	        	
	        	out.write(line_out);
                out.newLine();
	        }
        
	    } catch (Exception e) {
	          System.out.println(e);
	    }	
	}
	
	public String getRelevantPos(String[] textArray){
		
		InputStream modelIn = null;		
		String[] tags;	
		String relevantWords = "";

		try {
			modelIn = new FileInputStream(System.getProperty("user.dir") + "/../models/en-pos-maxent.bin");
			POSModel model = new POSModel(modelIn);
			
			POSTaggerME tagger = new POSTaggerME(model);
			tags = tagger.tag(textArray);
			
			if(textArray.length != tags.length)
				throw new Exception();
			
			for(int i=0; i < tags.length; i++){

				if(tags[i].equals("JJ") || tags[i].equals("JJR") || tags[i].equals("JJS") ||
						tags[i].equals("RB") || tags[i].equals("RBR") || tags[i].equals("RBS")){
					
					relevantWords = relevantWords + " " + textArray[i];
				}
			}
			
			return relevantWords;
		}
		catch (IOException e) {
			e.printStackTrace();
			System.out.println("[Error] OpenNLP POS tagger model loading failed");
			return "";
		}
		catch (Exception e){
			e.printStackTrace();
			System.out.println("[Error] Part of speech tagging error");
			return "";
		}
		finally {
			if (modelIn != null) {
				
				try {
		    		modelIn.close();
				}
				catch (IOException e) {	}
			}
		}
	}
}
