Program Laby;
Uses Crt;
Var screen : Array [0..9, 0..19] of Char;
Var key : Char;
Var posx, posy, i, i2 : Integer;
Var fichier : Text;
Var ligne : String;
BEGIN
    Assign(fichier, 'level.txt');
    Reset(fichier);

    for i := 0 to 9 do
    begin
        ReadLn(fichier, ligne);
        for i2 := 1 to 20 do
        begin
            screen[i][i2 - 1] := ligne[i2];
        end
    end;

    Close(fichier);

    posx := 1;
    posy := 1;
    key := 'a';

    repeat

        if key = 's' then
        begin
            if screen[posx + 1][posy] = '-' then
            begin
                screen[posx][posy] := '-';
                screen[posx + 1][posy] := '@';
                posx := posx + 1;
            end
            else if screen[posx + 1][posy] = 'a' then
            begin
                writeln('GAGNE !');
                break;
            end;
        end

        else if key = 'z' then
        begin
            if screen[posx - 1][posy] = '-' then
            begin
                screen[posx][posy] := '-';
                screen[posx - 1][posy] := '@';
                posx := posx - 1;
            end
            else if screen[posx - 1][posy] = 'a' then
            begin
                writeln('GAGNE !');
                break;
            end;
        end

        else if key = 'q' then
        begin
            if screen[posx][posy - 1] = '-' then
            begin
                screen[posx][posy] := '-';
                screen[posx][posy - 1] := '@';
                posy := posy - 1;
            end
            else if screen[posx][posy - 1] = 'a' then
            begin
                writeln('GAGNE !');
                break;
            end;
        end

        else if key = 'd' then
        begin
            if screen[posx][posy + 1] = '-' then
            begin
                screen[posx][posy] := '-';
                screen[posx][posy + 1] := '@';
                posy := posy + 1;
            end
            else if screen[posx][posy + 1] = 'a' then
            begin
                writeln('GAGNE !');
                break;
            end;
        end;

        ClrScr;

        for i := 0 to 9 do
        begin
            for i2 := 0 to 19 do
            begin
                write(screen[i][i2]);
            end;
            writeln;
        end;

        key := ReadKey;
            
    until key = 'x'
END. 