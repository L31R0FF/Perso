Program Exemple28;

Uses 
  Crt;

Var 
  i, j : Integer;
  x : Real;
  Test : Boolean;

Procedure Menu (Page : Integer; Test : Boolean) ;
Begin
  WriteLn('*===================================================================*');
  WriteLn('|                        SuperCalculator 2.5                        |');
  WriteLn('*===================================================================*');
  if Test then 
    WriteLn('Faire afficher le menu principal...')
  else
    begin
      WriteLn('+--------------------------------------------------+----------------+');
      WriteLn('¦  Module : CALCUL DE FONCTION                     ¦   Page :   ',Page,'   ¦');
      WriteLn('+------------------------+-------------------------+----------------+');
      WriteLn('¦      Valeur de X       ¦     Valeur de Y=f(X)    ¦');
      WriteLn('¦                        ¦                         ¦');
    end ;
End;

Function f (x : Real) : Real;
Begin
  f := Sqr(x);
End;

BEGIN
  ClrScr;
  i := 0;
  j := 1;
  Test := False;
  Menu(j,Test) ;
  x := 0;
  repeat
    Inc(i);
    x := x + 50;
    WriteLn('¦      ',Round(x):12,'       ¦     ',Round(f(x)):16,'   ¦');
    Test := x > 1700;
    if ((i Mod 14) = 0) or test then
      begin
        WriteLn('+------------------------+-------------------------+');
        WriteLn('¦      Appuyez sur <ENTREE> pour continuer...      ¦');
        WriteLn('+--------------------------------------------------+');
        ReadLn;
        ClrScr;
        Inc(j);
        Menu(j,Test);
      end;
  until Test;
  ReadLn;
END.