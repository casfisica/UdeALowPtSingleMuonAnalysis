# include <cstdlib>  // needed to convert string argument to integer
# include <iostream>
// # include "libraries_from user"

using namespace std;

void Trigger_Paths_Analysis( const char *inputFile )
{
  /********************************************//**
  *  coments for Doxygen
  ***********************************************/

  //gSystem->Load("libDelphes"); //Done in the rootlogon.C
  
  // Create chain of root trees
  TChain chain("Delphes");
  chain.Add(inputFile);

  // Create object of class ExRootTreeReader
  ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
  Long64_t numberOfEntries = treeReader->GetEntries();

  // Get pointers to branches used in this analysis
  TClonesArray *branchJet = treeReader->UseBranch("Jet");
  TClonesArray *branchElectron = treeReader->UseBranch("Electron");

  // Book histograms
  TH1 *histJetPT = new TH1F("jet_pt", "jet P_{T}", 100, 0.0, 100.0);
  TH1 *histMass = new TH1F("mass", "M_{inv}(e_{1}, e_{2})", 100, 40.0, 140.0);
  


}




///////////////////////////////////////////////////////////////////////////////////////////////////////
//********************************FOR THE COMPILER***************************************************//
///////////////////////////////////////////////////////////////////////////////////////////////////////

// compile with:  g++ -o program_name.C `root-config --cflags --glibs`

# ifndef __CINT__  // the following code will be invisible for the interpreter

#include "classes/DelphesClasses.h" //the heders of delphes
#include "external/ExRootAnalysis/ExRootTreeReader.h"

int main(int argc, char *argv)
{
  if (argc == 1)  // no parameter given
    {
      cout << "need a file.root as the imput";
      return 1;
    }
  else
    {
      //Parametriced function
      
      
    }
}

# endif
