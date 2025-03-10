#region imports
from ResistorNetwork import ResistorNetwork, ResistorNetwork_2
#endregion

# region Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
    """
    print("Network 1:")
    Net= ResistorNetwork()  #Instantiating a ResistorNetwork object
    Net.BuildNetworkFromFile("ResistorNetwork.txt")  # Building the network from the file
    IVals=Net.AnalyzeCircuit() # Solve for unknown currents

    print("\nNetwork 2:")
    Net_2 = ResistorNetwork_2()  #Instantiating a ResistorNetwork_2 object
    Net_2.BuildNetworkFromFile("ResistorNetwork.txt")  # Building the network from the file
    IVals_2=Net_2.AnalyzeCircuit() # Solving for the unknown
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion