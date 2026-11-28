import subprocess
from argparse import ArgumentParser

def load_instance(input_file_name):
    # read the input instance
    edges = [] #more precisely, this will be a list where the first item is the number of vertices and the next items are the edges with start and end vertex
    with open(input_file_name, "r") as file:
        for line in file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                edges.append(line)
    return edges
"""
def encode(instance):
    # given the instance, create a cnf formula, i.e. a list of lists of integers
    # also return the total number of variables used

    cnf = []

    # no two tiles are at the same place at the same time, i.e. at most 1 of n is in p, t
    for t in range(MAKESPAN+1):
        for p in range(NR_TILES):
            for n1 in range(NR_TILES):
                for n2 in range(n1+1, NR_TILES):
                    cnf.append([-pos_to_atID(n1,p,t), -pos_to_atID(n2,p,t)])

    # a tile can not be at two places at the same time, i.e. at most 1 of p is in n, t
    for t in range(MAKESPAN+1):
        for n in range(NR_TILES):
            for p1 in range(NR_TILES):
                for p2 in range(p1+1, NR_TILES):
                    cnf.append([-pos_to_atID(n,p1,t), -pos_to_atID(n,p2,t)])

    return (cnf, nr_vars)
"""
def call_solver(cnf, nr_vars, output_name, solver_name, verbosity):
    # print CNF into formula.cnf in DIMACS format
    with open(output_name, "w") as file:
        file.write("p cnf " + str(nr_vars) + " " + str(len(cnf)) + '\n')
        for clause in cnf:
            file.write(' '.join(str(lit) for lit in clause) + '\n')

    # call the solver and return the output
    return subprocess.run(['./' + solver_name, '-model', '-verb=' + str(verbosity) , output_name], stdout=subprocess.PIPE)

#edit
def print_result(model):
    return (model is not None) #there exists a model of the problem -> true, otherwise false

if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument(
        "-i",
        "--input",
        default="instances/input.in",
        type=str,
        help=(
            "The instance file."
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        default="formula.cnf",
        type=str,
        help=(
            "Output file for the DIMACS format (i.e. the CNF formula)."
        ),
    )
    parser.add_argument(
        "-s",
        "--solver",
        default="solver",
        type=str,
        help=(
            "The SAT solver to be used."
        ),
    )
    parser.add_argument(
        "-v",
        "--verb",
        default=1,
        type=int,
        choices=range(0,2),
        help=(
            "Verbosity of the SAT solver used."
        ),
    )
    args = parser.parse_args()

    # get the input instance
    instance = load_instance(args.input)
    N_edges = instance[0][0]
    edges = instance[1:]

    # encode the problem to create CNF formula
    cnf, nr_vars = encode(instance)

    # call the SAT solver and get the result
    result = call_solver(cnf, nr_vars, args.output, args.solver, args.verb)

    # interpret the result and print it in a human-readable format
    print_result(result)