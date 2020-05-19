function getfile(const FileName: string): Boolean;
var
  S: TStringList;
  i: Integer;
begin
  Result:= False;
  if FileExists(FileName) then begin
    S:= TStringList.Create;
    S.LoadFromFile(FileName);
    FScr.Script:= S;
    Result:= FScr.Compile;
    for i:= 0 to aPSCE.FScr.CompilerMessageCount - 1 do
      writeln(aPSCE.FScr.CompilerMessages[i].MessageToString);
    S.Free;
    if not Result then
      if FScr.CompilerMessageCount > 0 then
        for i:= 0 to FScr.CompilerMessageCount-1 do
          Writeln(FScr.CompilerErrorToStr(i));
      end else Writeln('Script File not found: ', FileName);
end;