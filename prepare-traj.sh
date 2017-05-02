
#!/bin/bash

struct="all.psf"
coor="all.pdb"


#..1 wrap all trajectories 
for file in $(seq 1 $(ls prod*.dcd | wc -l)) ; do 

  file=$(printf "%02d" $file)
  if [ -f wrap${file}.dcd ] ; then 
    echo "info: wrap${file}.dcd already exists. Taken as is."
  else 
  echo "info: wrapping trajectory prod${file}.dcd" 
  vmd -dispdev text << EOF
# tcl script for vmd

package require pbctools
atomselect macro ec_sheet   { name CA and resid 29 to 35  53 to 59  118 to 123  141 to 150  202 to 210 }
atomselect macro tm_helices { name CA and resid 218 to 235  242 to 265  274 to 299}
atomselect macro core      { ec_sheet or tm_helices }
set step 1
set ifile prod${file}.dcd 
  
# read mol and wrap trajectory
mol new $struct type psf
mol addfile \$ifile type dcd first 0 last -1 step \$step filebonds 1 autobonds 1 waitfor all

# procedure called at each frame 
 pbc wrap -compound fragment -center com -centersel "segname E" -all -sel "protein"
 pbc wrap -compound fragment -center com -centersel "protein" -all 


 animate write dcd wrap${file}.dcd waitfor all 
 quit
EOF
  fi

done 

#..2 align all traj

for file in $(ls wrap*.dcd) ; do 

  if [ -f aligned_$file ] ; then 
    echo "info: aligned_$file already exists. Taken as is."
  else
    echo "info: aligning traj ${file}." 
    wordom -ia rmsd --SELE "/*/@(218-235|242-265|274-299)/CA" -imol $coor -itrj $file --TRJOUT aligned_${file}
  fi

done 

#..3 create the protein+IVM trajectory

ls aligned_wrap*.dcd > tmp.txt
echo "info: creating merged trajectory of the protein + IVM"
wordom -F all -imol $coor -itrj tmp.txt -sele "//@(A|B|C|D|E|AAA|BBB|CCC|DDD|EEE)//" -otrj protein_full.dcd

echo "info: creating protein PDB and PSF" 
vmd -dispdev text << EOF
mol new $struct type psf
mol addfile $coor type pdb
set sel [atomselect top "segname A B C D E AAA BBB CCC DDD EEE"]
\$sel writepdb protein.pdb
\$sel writepsf protein.psf
EOF

rm tmp.txt
