import sa.dataprocessing.AutoCorrect;
import sa.postag.PosTagger;

public class saMain {

	/**
     * AutoCorrect class
     * Uses Jazzy-0.5.2 library to perform a spell-check on text and auto-correct
     * in case of an spelling error/typo by replacing the typo with the first suggestion, if there exists one.
     */
	public static void main(String[] args) {
						
		if(args.length != 3) {
			System.out.println("incorrect parameters provided");
			return;
		}
		
		System.out.println(args[0]);
		System.out.println(args[1]);
		System.out.println(args[2]);
	
		if(args[0].equals("s")){
			
			System.out.println("Running spell check against DoubleMeta");
			new AutoCorrect(args[1],args[2]);	
		}
		else if(args[0].equals("pos")){
			System.out.println("Running part of speech tagging");
			new PosTagger(args[1],args[2]);
		}
	}

}
