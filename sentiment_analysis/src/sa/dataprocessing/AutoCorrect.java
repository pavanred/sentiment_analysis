
/*
Jazzy - a Java library for Spell Checking
Copyright (C) 2001 Mindaugas Idzelis
Full text of license can be found in LICENSE.txt

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

package sa.dataprocessing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.List;

import com.swabunga.spell.engine.SpellDictionary;
import com.swabunga.spell.engine.SpellDictionaryHashMap;
import com.swabunga.spell.event.SpellCheckEvent;
import com.swabunga.spell.event.SpellCheckListener;
import com.swabunga.spell.event.SpellChecker;
import com.swabunga.spell.event.StringWordTokenizer;

public class AutoCorrect implements SpellCheckListener {

	private static String DICT_FILE =
			System.getProperty("user.dir") + "/../models/eng_com.dic";
	
	 private SpellChecker spellCheck = null;
     FileWriter fstream;
     BufferedWriter out;
     String line_out = "";   

	public AutoCorrect(String INPUT_FILE, String OUTPUT_FILE) {
        try {
            
            fstream = new FileWriter(OUTPUT_FILE);
                    out = new BufferedWriter(fstream);
                            
                BufferedReader in = new BufferedReader(new FileReader(INPUT_FILE));
                File phonetic = null;
                
                SpellDictionary dictionary = new SpellDictionaryHashMap(new File(DICT_FILE), phonetic);
                spellCheck = new SpellChecker(dictionary);
                spellCheck.addSpellCheckListener(this);

                while (true) {
                    String line_input = in.readLine();
                    line_out = line_input;
                    
                    if (line_input == null || line_input.length() == -1)
                        break;
    
                    spellCheck.checkSpelling(new StringWordTokenizer(line_input));
                                        
                    out.write(line_out);
                    out.newLine();
                }
                
          in.close();
          out.close();
          
        } catch (Exception e) {
          System.out.println(e);
        }
    }

	@Override
	public void spellingError(SpellCheckEvent event) {
		
		try{
		
			List suggestions = event.getSuggestions();
        
			if (suggestions.size() > 0) {
          
				String suggest = "";
          
				//most commonly used T9 dict typos
				if(event.getInvalidWord().toString() == "y" || event.getInvalidWord().toString() == "Y")
                    suggest = "why";
				else if(event.getInvalidWord().toString() == "d" || event.getInvalidWord().toString() == "D")
                    suggest = "the";
				else
                    suggest = suggestions.get(0).toString();
          
				line_out = line_out.replaceFirst(event.getInvalidWord().toString(), suggest);
            
				System.out.println("Replacing " + event.getInvalidWord() + " with " + suggest) ;              
			}
		} catch (Exception e) {
        System.out.println(e);
      }
	}

}
