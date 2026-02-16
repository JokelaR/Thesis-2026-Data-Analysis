# About
This is a repository for the data analysis workbook used for my 2026 Master's Thesis into layuser perceptions of Generative Artificial Intelligence. The final paper can be found [here](https://urn.fi/URN:NBN:fi:oulu-202602121740).

No data is provided with the workbook, but the format used for the study is described below in the _Data format_ section.

<img width="1322" height="575" alt="image" src="https://github.com/user-attachments/assets/18af4b2c-1832-4383-badf-c471e6a216a3" />


# Replicating the environment
This [Marimo](https://marimo.io/) workbook requires the installation of the [uv](https://github.com/astral-sh/uv) Python project manager utility. 

After uv is installed, you can run the workbook by navigating into the project folder and invoking the Marimo editor with 
```bash
uv run marimo edit .\masters.py
```
This will automatically download all the necessary dependencies and open the workbook in your browser of choice.

# Data format
The workbook relies on specific base data to run, derived from the Google Forms sheet output format used. The list of columns can be seen below, which are at workbook start loaded from `responses.xlsx`. 
The scripts also rely on various assumptions regarding the specific contents of the data, so while some functions are relatively resilient against missing data points, some work might be required to produce identical outputs if some specific field contents are not present.

```
 [1] "Timestamp" 
 [2] "Age (Years)" 
 [3] "Gender" 
 [4] "Select any or all groups that apply to you" 
 [5] "Country of residence (Optional)" 
 [6] "Countries.Normalized" 
 [7] "Region" 
 [8] "How many hours would you estimate you spend per day using personal computing devices (computer, phone, tablet), including work?"
 [9] "How would you describe your \"computer literacy\" (skill at operating computers, phones, and similar smart devices)?" 
[10] "Have you ever participated in the production of a creative work (visual or musical art, performance, etc.)?" 
[11] "Have you previously utilized generative artificial intelligence tools?" 
[12] "If yes, please name one or more (Optional)" 
[13] "Which methods have you used to interact with generative AI?" 
[14] "Have you previously participated in or ran studies involving generative artificial intelligence?" 
[15] "What is your current opinion of generative artificial intelligence tools?" 
[16] "In a few short sentences, elaborate on your current opinion (optional)" 
[17] "Scenario 1 [This system is an example of generative AI]" 
[18] "Scenario 1 [I did the majority of the work]" 
[19] "Scenario 1 [I played a key part in the creation of the output]" 
[20] "Scenario 1 [The output represents my creative vision]" 
[21] "Scenario 1 [I would describe the output as my own]" 
[22] "Scenario 1 [I was in control of the output]" 
[23] "Scenario 1 [I know about a real service or feature like this]" 
[24] "Scenario 1 [I have used a service or feature like this]" 
[25] "Scenario 2 [This system is an example of generative AI]" 
[26] "Scenario 2 [I did the majority of the work]" 
[27] "Scenario 2 [I played a key part in the creation of the output]" 
[28] "Scenario 2 [The output represents my creative vision]" 
[29] "Scenario 2 [I would describe the output as my own]" 
[30] "Scenario 2 [I was in control of the output]" 
[31] "Scenario 2 [I know about a real service or feature like this]" 
[32] "Scenario 2 [I have used a service or feature like this]" 
[33] "Scenario 3 [This system is an example of generative AI]" 
[34] "Scenario 3 [I did the majority of the work]" 
[35] "Scenario 3 [I played a key part in the creation of the output]" 
[36] "Scenario 3 [The output represents my creative vision]" 
[37] "Scenario 3 [I would describe the output as my own]" 
[38] "Scenario 3 [I was in control of the output]" 
[39] "Scenario 3 [I know about a real service or feature like this]" 
[40] "Scenario 3 [I have used a service or feature like this]" 
[41] "Scenario 4 [This system is an example of generative AI]" 
[42] "Scenario 4 [I did the majority of the work]" 
[43] "Scenario 4 [I played a key part in the creation of the output]" 
[44] "Scenario 4 [The output represents my creative vision]" 
[45] "Scenario 4 [I would describe the output as my own]" 
[46] "Scenario 4 [I was in control of the output]" 
[47] "Scenario 4 [I know about a real service or feature like this]" 
[48] "Scenario 4 [I have used a service or feature like this]" 
[49] "Scenario 5 [This system is an example of generative AI]" 
[50] "Scenario 5 [I did the majority of the work]" 
[51] "Scenario 5 [I played a key part in the creation of the output]" 
[52] "Scenario 5 [The output represents my creative vision]" 
[53] "Scenario 5 [I would describe the output as my own]" 
[54] "Scenario 5 [I was in control of the output]" 
[55] "Scenario 5 [I know about a real service or feature like this]" 
[56] "Scenario 5 [I have used a service or feature like this]" 
[57] "Open feedback (Optional)" 
[58] "Sentiments.In a few short sentences, elaborate on your current opinion (optional" 
[59] "Sentiments.Sentiment" 
[60] "Sentiments.Bad Output" 
[61] "Sentiments.Theft" 
[62] "Sentiments.Environment" 
[63] "Sentiments.Human replacement" 
[64] "Sentiments.Economy" 
[65] "Sentiments.Sycophancy Mental harm" 
[66] "Sentiments.Disinfo" 
[67] "Sentiments.Other Ethics" 
[68] "Sentiments.Forced on you" 
[69] "Sentiments.Oversold" 
[70] "Sentiments.Toy" 
[71] "Sentiments.\"Outweigh\" / Net Negative" 
[72] "Sentiments.Negative view of owners" 
[73] "Sentiments.Negative image of users" 
[74] "Sentiments.General concerns" 
[75] "Sentiments.Valid formal uses" 
[76] "Sentiments.Slop hose" 
[77] "Sentiments.Regulation" 
```
