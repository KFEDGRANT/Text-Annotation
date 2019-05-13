#https://answers.microsoft.com/en-us/msoffice/forum/msoffice_word-mso_win10-mso_o365b/bulk-convert-doc-files-to-docx-in-word-2016/1c5628bc-c2ea-4072-bb25-56eae952d2c5
#VBA code, to be executed in Microsoft Office Visual Basic Editor
#Converts .doc files to .docx to be processed into .txt for Comprehend analysis
Sub TranslateDocIntoDocx()
  Dim objWordApplication As New Word.Application
  Dim objWordDocument As Word.Document
  Dim strFile As String
  Dim strFolder As String

  strFolder = #insert file path here
  strFile = Dir(strFolder & "*.doc", vbNormal)

  While strFile <> ""
    With objWordApplication      
      Set objWordDocument = .Documents.Open(FileName:=strFolder &strFile, AddToRecentFiles:=False, ReadOnly:=True, Visible:=False)

      With objWordDocument
        .SaveAs FileName:=strFolder & Replace(strFile, "doc", "docx"), FileFormat:=16
        .Close
      End With
    End With
    strFile = Dir()
  Wend   

  Set objWordDocument = Nothing
  Set objWordApplication = Nothing
End Sub
