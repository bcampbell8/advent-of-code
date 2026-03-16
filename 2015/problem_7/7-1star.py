#The list of instructions is given in an unsorted list.
#Applying each wire in alphabetical order is how wires are derived, with the
#exception of wire 'a', which is solved last.
import pdb
instructions = {}
with open("input.md", "r", encoding="utf-8") as f:
    for line in f:
        components = line.split(" ")
        instructions[f"{components[-1].strip("\n")}"] = line
evaluated_ins = {}
secondletter = None
def evaluate_wires():
    #Set two loops to evaluate each wire sequentially.
    #The first loop represents iterations with wires that have more than one
    #letter as a name e.g 'ab', in which it represents the first character
    #The second loop represents the second character. It represents 'b' in the
    #string 'ab', but it is also what is used for the single named wires.
    for h in range (0, 13):
        if h != 0:
            secondletter = 96 + h
        for i in range(97,123):
            if (h == 0 and i == 97):
                continue
            if (h == 0):
                wire = instructions[f"{chr(i)}"].split("->")
            else:
                wire = instructions[f"{chr(secondletter)}" + \
                    f"{chr(i)}"].split("->")
            #This checks for if the instruction is a purely numeric signal
            #provided to a wire.
            if len(wire[0].strip().split(" ")) == 1 and \
                wire[0].strip().isnumeric():
                evaluated_ins[f"{wire[1].strip("\n").strip()}"] = int(wire[0])
            else:
                wire_words = wire[0].split(" ")
                #This checks for the exceptional case of if an instruction is
                #NOT, which only has two words that compose the instruction.
                if wire_words[0].isupper() == True:
                    evaluated_ins[f"{wire[1].strip("\n").strip()}"] = \
                        ~evaluated_ins[wire_words[1].strip()]
                else:
                    #Format words, removing white space and then evaluate
                    #expression based on bitwise operator.
                    if wire_words[0].strip().isalpha():
                        word1 = evaluated_ins[f"{wire_words[0].strip()}"]
                    else:
                        word1 = int(wire_words[0].strip())
                    if wire_words[2].strip().isalpha():
                        word3 = evaluated_ins[f"{wire_words[2].strip()}"]
                    else:
                        word3 = int(wire_words[2].strip())
                    match wire_words[1].strip():
                        case 'AND':
                            evaluated_ins[f"{wire[1].strip().strip("\n")}"] = \
                                word1 & word3
                        case 'OR':
                            evaluated_ins[f"{wire[1].strip().strip("\n")}"] = \
                                word1 | word3
                        case 'LSHIFT':
                            evaluated_ins[f"{wire[1].strip().strip("\n")}"] = \
                                word1 << word3
                        case 'RSHIFT':
                            evaluated_ins[f"{wire[1].strip().strip("\n")}"] = \
                                word1 >> word3
evaluate_wires()
print(f"Wire a receives a signal of: {evaluated_ins['lx']}")

#2 star solution
instructions['b'] = f"{evaluated_ins['lx']} -> b"
evaluate_wires()
print(f"Wire a receives a new signal of {evaluated_ins['lx']}")

