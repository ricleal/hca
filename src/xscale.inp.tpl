!============ XSCALE.INP : maximum user input
!
! Original here : http://xds.mpimf-heidelberg.mpg.de/html_doc/INPUT_templates/XSCALE.INP
!
!
!MAXIMUM_NUMBER_OF_PROCESSORS=16
!RESOLUTION_SHELLS= 10 6 4 3 2.5 2.0 1.8 1.7 1.6
!SPACE_GROUP_NUMBER=19
!UNIT_CELL_CONSTANTS=65.46 108.41 113.15   90.000  90.000  90.000
!REIDX=-1 0 0 0    0 -1 0 0    0 0 -1 0
!REFERENCE_DATA_SET= fae-rm.ahkl

!MINIMUM_I/SIGMA=3.0
!REFLECTIONS/CORRECTION_FACTOR=50   !minimum #reflections/correction_factor
!0-DOSE_SIGNIFICANCE_LEVEL=0.10
!WFAC1=1.5 ! factor applied to e.s.d.'s before testing equivalent reflections

OUTPUT_FILE= $output_file
   FRIEDEL'S_LAW= $friedels_law_value  !FALSE !TRUE
!  MERGE=FALSE !TRUE
!  STRICT_ABSORPTION_CORRECTION=TRUE  !FALSE is default
#foreach ($input_file in $input_files)
   INPUT_FILE= $input_file
!    INCLUDE_RESOLUTION_RANGE= 20 1.6
!    CORRECTIONS= DECAY MODULATION ABSORPTION
!    CRYSTAL_NAME=Seleno1 !Remove first "!" to switch on 0-dose extrapolation
!    STARTING_DOSE=0.0  DOSE_RATE=1.0  !Use defaults for 0-dose extrapolation
#end
