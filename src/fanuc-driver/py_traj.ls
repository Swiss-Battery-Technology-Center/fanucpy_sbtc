/PROG  PY_TRAJ
/ATTR
OWNER		= MNEDITOR;
COMMENT		= "";
PROG_SIZE	= 486;
CREATE		= DATE 25-05-02  TIME 08:13:32;
MODIFIED	= DATE 25-05-02  TIME 11:28:24;
FILE_NAME	= ;
VERSION		= 0;
LINE_COUNT	= 18;
MEMORY_SIZE	= 918;
PROTECT		= READ_WRITE;
TCD:  STACK_SIZE	= 0,
      TASK_PRIORITY	= 50,
      TIME_SLICE	= 0,
      BUSY_LAMP_OFF	= 0,
      ABORT_REQUEST	= 0,
      PAUSE_REQUEST	= 0;
DEFAULT_GROUP	= 1,*,*,*,*;
CONTROL_CODE	= 00000000 00000000;
/APPL
  SPOT : TRUE ; 
  SPOT Welding Equipment Number : 1 ;
/MN
   1:  WAIT   1.00(sec) ;
   2:  MESSAGE[Hello] ;
   3:  LBL[1] ;
   4:  MESSAGE[Waiting for traj] ;
   5:  WAIT (F[81:ON ])    ;
   6:  MESSAGE[Start traj] ;
   7:  R[86]=R[84]    ;
   8:  LBL[2] ;
   9:  IF (R[86]>R[87]) THEN ;
  10:  WAIT    .01(sec) ;
  11:  JMP LBL[2] ;
  12:  ENDIF ;
  13:J PR[R[86]] R[81]% CNT R[83] ACC R[82]    ;
  14:  R[86]=R[86]+1    ;
  15:  IF R[86]<R[85],JMP LBL[2] ;
  16:J PR[R[86]] R[81]% FINE ACC R[82]    ;
  17:  F[81:ON ]=(OFF) ;
  18:  JMP LBL[1] ;
/POS
/END
