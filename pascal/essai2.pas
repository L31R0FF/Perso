Program CAR;
Uses Crt;
Var i : Integer;
BEGIN
    for i := 10 downto 1 do
    begin
        WriteLn(i);
        Delay(1000);
    end;
    Writeln('BOOOOM !!!');
    Sound(512);
    Delay(500);
END.