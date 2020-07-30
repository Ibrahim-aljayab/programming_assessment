# component 6 - Statement Generator
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main routine
print()
well_done = hl_statement("*** correct ***", "*")

print()
start_round = hl_statement("### Round 1 of 3 ###", "#")
