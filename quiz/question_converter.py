import json
import os
import re

input_folder = os.getcwd()
output_file = "GIFT/neuroscience_exam.gift"

def two_words(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return "_".join(words[:2])

with open(output_file,"w",encoding="utf8") as out:

    for file in os.listdir(input_folder):

        if file.endswith(".json"):

            topic = file.split("_")[1].replace(".json","")

            with open(os.path.join(input_folder,file)) as f:
                data = json.load(f)

            out.write(f"$CATEGORY: module_1_multi/{topic}\n\n")

            for q in data["questions"]:

                name = f"{topic}_{two_words(q['question'])}"

                out.write(f"::{name}::\n")
                out.write(q["question"]+"\n{\n")

                for i,opt in enumerate(q["options"]):

                    if i == q["correct"]:
                        if "feedback" in q:
                            out.write(f"={opt} #{q['feedback']}\n")
                        else:
                            out.write(f"={opt}\n")
                    else:
                        out.write(f"~{opt}\n")

                out.write("}\n\n")

print("GIFT file ready")