$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$wb = $excel.Workbooks.Open('D:\Projects\Lab\Track 1\Track1_Day26_2A202601742_NguyenVuVietAnh\Track1_Day25_2A202601742_NguyenVuVietAnh\NguyenVuVietAnh_Day25_model.xlsx')
foreach ($ws in $wb.Worksheets) {
    Write-Host "=== Sheet: $($ws.Name) ==="
    $used = $ws.UsedRange
    for ($r = 1; $r -le $used.Rows.Count; $r++) {
        $rowData = @()
        for ($c = 1; $c -le [math]::Min(15, $used.Columns.Count); $c++) {
            $cell = $ws.Cells.Item($r, $c)
            if ($cell.Value2 -ne $null) {
                $rowData += "$($cell.Address): $($cell.Value2)"
            }
        }
        if ($rowData.Count -gt 0) {
            Write-Host ($rowData -join ' | ')
        }
    }
    Write-Host ""
}
$wb.Close($false)
$excel.Quit()