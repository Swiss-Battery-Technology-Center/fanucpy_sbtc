/PROG  PY_TRAJ
/ATTR
OWNER		= MNEDITOR;
COMMENT		= "";
PROG_SIZE	= 640;
CREATE		= DATE 25-05-02  TIME 08:13:32;
MODIFIED	= DATE 25-05-02  TIME 16:24:30;
FILE_NAME	= ;
VERSION		= 0;
LINE_COUNT	= 26;
MEMORY_SIZE	= 1040;
PROTECT		= READ_WRITE;
TCD:  STACK_SIZE	= 0,
      TASK_PRIORITY	= 50,
      TIME_SLICE	= 0,
      BUSY_LAMP_OFF	= 0,
      ABORT_REQUEST	= 0,
      PAUSE_REQUEST	= 0;
DEFAULT_GROUP	= *,*,*,*,*;
CONTROL_CODE	= 00000000 00000000;
/APPL
  SPOT : TRUE ; 
  SPOT Welding Equipment Number : 1 ;
/MN
   1:  LBL[1] ;
   2:  F[81:OFF]=(OFF) ;
   3:  MESSAGE[Waiting for trajectory] ;
   4:  WAIT (F[81:OFF])    ;
   5:  MESSAGE[Start trajectory] ;
   6:  R[86]=R[84]    ;
   7:  LBL[2] ;
   8:  IF (R[86]>R[87]) THEN ;
   9:  WAIT    .01(sec) ;
  10:  JMP LBL[2] ;
  11:  ENDIF ;
  12:  IF R[86]=0,JMP LBL[1] ;
  13:  IF (F[82:OFF]) THEN ;
  14:L PR[R[86]] R[81]mm/sec CNT R[83] ACC R[82]    ;
  15:  ELSE ;
  16:J PR[R[86]] R[81]% CNT R[83] ACC R[82]    ;
  17:  ENDIF ;
  18:  R[86]=R[86]+1    ;
  19:  IF R[86]<R[85],JMP LBL[2] ;
  20:  IF (F[82:OFF]) THEN ;
  21:L PR[R[85]] R[81]mm/sec FINE ACC R[82]    ;
  22:  ELSE ;
  23:J PR[R[85]] R[81]% FINE ACC R[82]    ;
  24:  ENDIF ;
  25:  F[81:OFF]=(OFF) ;
  26:  JMP LBL[1] ;
/POS
/END
