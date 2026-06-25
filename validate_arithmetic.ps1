# validate_arithmetic.ps1
# Valida todas las cadenas de calculo de report-source.md
# Uso: .\validate_arithmetic.ps1
# Salida: PASS/FAIL por cada chequeo + resumen

$ErrorActionPreference = 'Continue'
$script:fail = 0
$script:pass = 0
$script:warnings = 0

function Check {
    param(
        [string]$Id,
        [double]$Computed,
        [double]$Reported,
        [double]$Tolerance = 1.5,
        [string]$Note = ''
    )
    $delta = [math]::Abs($Computed - $Reported)
    $pct = if ($Reported -ne 0) { [math]::Round($delta / [math]::Abs($Reported) * 100, 2) } else { 0 }
    
    if ($delta -le $Tolerance) {
        Write-Output "  PASS  $Id : computed=$([math]::Round($Computed,2)) reported=$Reported delta=$([math]::Round($delta,2)) $Note"
        $script:pass++
    }
    else {
        Write-Output "  FAIL  $Id : computed=$([math]::Round($Computed,2)) reported=$Reported delta=$([math]::Round($delta,2)) ($pct%) $Note"
        $script:fail++
    }
}

function Warn {
    param([string]$Id, [string]$Msg)
    Write-Output "  WARN  $Id : $Msg"
    $script:warnings++
}

Write-Output "============================================================"
Write-Output " VALIDACION ARITMETICA - report-source.md"
Write-Output "============================================================"
Write-Output ""

# ----------------------------------------------------------
# §2.4 Escenario Base (antes "Conservador")
# ----------------------------------------------------------
Write-Output "--- §2.4 Escenario BASE ---"
Check -Id "BASE-1" -Computed (3182 * 0.66) -Reported 2100 -Note "3182*66% padres"
Check -Id "BASE-2" -Computed (3182 * 0.66 * 1.4) -Reported 2940 -Note "3182*66%*1.4 hijos"

# ----------------------------------------------------------
# §2.4 Escenario Restricción — 1.0.0 corregido
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §2.4 Escenario RESTRICCION ---"
Check -Id "RES-1" -Computed (4474 * 0.66) -Reported 2953 -Tolerance 1 -Note "4474*66% prohibicion acercamiento"
Check -Id "RES-2" -Computed (4474 * 0.66 * 1.4) -Reported 4134 -Tolerance 2 -Note "4474*66%*1.4 = NNyA restriccion"

# ----------------------------------------------------------
# §2.4 Escenario Techo (antes "Amplio")
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §2.4 Escenario TECHO ---"
$amp_step1 = 33763 * 0.71
Check -Id "AMP-1" -Computed $amp_step1 -Reported 23972 -Note "33763*71% padres"
$amp_step2 = [math]::Round($amp_step1, 0) * 0.60
Check -Id "AMP-2" -Computed $amp_step2 -Reported 14383 -Note "*60% con hijos (supuesto)"
$amp_step3 = [math]::Round($amp_step2, 0) * 0.85
Check -Id "AMP-3" -Computed $amp_step3 -Reported 12226 -Note "*85% interrupcion (supuesto)"
$amp_step4 = [math]::Round($amp_step3, 0) * 0.35
Check -Id "AMP-4" -Computed $amp_step4 -Reported 4279 -Note "*35% cronificacion (supuesto)"
$amp_step5 = [math]::Round($amp_step4, 0) * 1.5
Check -Id "AMP-5" -Computed $amp_step5 -Reported 6419 -Note "*1.5 hijos"
Check -Id "AMP-EXACT" -Computed (33763 * 0.71 * 0.60 * 0.85 * 0.35 * 1.5) -Reported 6419 -Note "exacto"

# ----------------------------------------------------------
# §3.2 Victimas intrafamiliares
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §3.2 Victimas intrafamiliares ---"
Check -Id "VIC-1" -Computed (3219 * 0.565) -Reported 1819 -Note "3219*56.5%"

# ----------------------------------------------------------
# §4.1 FD / total penal
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §4.1 FD ---"
Check -Id "FD-1" -Computed (7517 / 8254672 * 100) -Reported 0.09 -Tolerance 0.01 -Note "FD/penal %"

# ----------------------------------------------------------
# §4.2 FD-VG/VI clasificados
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §4.2 FD-VG/VI ---"
Check -Id "FD-2" -Computed (588 / 6609 * 100) -Reported 8.9 -Tolerance 0.1 -Note "588/6609 %"

# ----------------------------------------------------------
# §4.3 Alternativo ~42%
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §4.3 Alternativo ~42% ---"
Check -Id "FD-ALT" -Computed (80 / 193 * 100) -Reported 41.5 -Tolerance 0.5 -Note "(42+33+5)/(108+76+9)"

# ----------------------------------------------------------
# §4.3 Santa Fe techo
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §4.3 Santa Fe techo ---"
Check -Id "FD-SF" -Computed (48 / 78 * 100) -Reported 61.5 -Tolerance 0.1 -Note "48/78 clasificados"
Check -Id "FD-SF-TOTAL" -Computed (48 / 440 * 100) -Reported 11 -Tolerance 1 -Note "48/440 sobre total (OVG dice 11%)"

# ----------------------------------------------------------
# §4.5 Tabla provincial - sumas y descuadres
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §4.5 Tabla provincial FD ---"
$prov = @(
    @('CABA', 108, 42, 66, 0),
    @('Chaco', 76, 33, 43, 0),
    @('Chubut', 81, 0, 81, 0),
    @('EntreRios', 114, 27, 49, 38),
    @('LaPampa', 18, 0, 18, 0),
    @('Misiones', 47, 3, 34, 10),
    @('Neuquen', 41, 13, 27, 1),
    @('PBA', 1673, 112, 1561, 0),
    @('RioNegro', 58, 13, 45, 0),
    @('Salta', 4307, 282, 4025, 0),
    @('SanJuan', 17, 3, 14, 0),
    @('SantaFe', 440, 48, 30, 362),
    @('SgoEstero', 31, 7, 24, 0),
    @('TdF', 9, 5, 4, 0)
)

$sTotal = 0; $sVG = 0; $sOtra = 0; $sSD = 0
foreach ($p in $prov) {
    $n = $p[0]; $t = $p[1]; $vg = $p[2]; $otra = $p[3]; $sd = $p[4]
    $computed = $vg + $otra + $sd
    Check -Id "FD-PROV-$n" -Computed $computed -Reported $t -Tolerance 0 -Note "VG+otra+SD=total?"
    $sTotal += $t; $sVG += $vg; $sOtra += $otra; $sSD += $sd
}
Check -Id "FD-SUM-TOTAL" -Computed $sTotal -Reported 7020 -Tolerance 0 -Note "suma total FD"
Check -Id "FD-SUM-VG" -Computed $sVG -Reported 588 -Tolerance 0 -Note "suma FD-VG/VI"
Check -Id "FD-SUM-OTRA" -Computed $sOtra -Reported 6021 -Tolerance 0 -Note "suma FD-otra"
Check -Id "FD-SUM-SD" -Computed $sSD -Reported 411 -Tolerance 0 -Note "suma sin datos"

# ----------------------------------------------------------
# §4.5 Porcentajes provinciales reportados
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §4.5 Porcentajes provinciales ---"
$pctChecks = @(
    @('CABA', 42, 108, 0, '39'),
    @('Chaco', 33, 76, 0, '43'),
    @('Chubut', 0, 81, 0, '0'),
    @('EntreRios', 27, 76, 38, '35.5'),
    @('LaPampa', 0, 18, 0, '0'),
    @('Misiones', 3, 37, 10, '8.1'),
    @('Neuquen', 13, 40, 1, '32'),
    @('PBA', 112, 1673, 0, '7'),
    @('RioNegro', 13, 58, 0, '22'),
    @('Salta', 282, 4307, 0, '7'),
    @('SanJuan', 3, 17, 0, '18'),
    @('SantaFe', 48, 78, 362, '61.5'),
    @('SgoEstero', 7, 31, 0, '23'),
    @('TdF', 5, 9, 0, '56')
)
foreach ($pc in $pctChecks) {
    $n = $pc[0]; $vg = $pc[1]; $clas = $pc[2]; $sd = $pc[3]; $repPct = $pc[4]
    if ($clas -gt 0) {
        $calcPct = [math]::Round($vg / $clas * 100, 1)
    } else {
        $calcPct = 0
    }
    Check -Id "FD-PCT-$n" -Computed $calcPct -Reported ([double]$repPct) -Tolerance 1.0 -Note "VG/clasificados"
}

# ----------------------------------------------------------
# §5 CePASI
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §5 CePASI ---"
Check -Id "CEPASI" -Computed (3219 * 0.742 * 0.001) -Reported 2 -Tolerance 0.5 -Note "3219*74.2%*0.1%"

# ----------------------------------------------------------
# §5 UFEM
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §5 UFEM ---"
Check -Id "UFEM-1" -Computed (0.15 * 19227) -Reported 2884 -Tolerance 1 -Note "15%*19227 SNIC"

# ----------------------------------------------------------
# §6 Marco A
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §6 Marco A ratios ---"
Check -Id "MA-BASE" -Computed (2940 / 1819) -Reported 1.62 -Tolerance 0.02 -Note "2940/1819 (Base)"
Check -Id "MA-RES" -Computed (4134 / 1819) -Reported 2.27 -Tolerance 0.02 -Note "4134/1819 (Restriccion)"
Check -Id "MA-TECHO" -Computed (6419 / 1819) -Reported 3.53 -Tolerance 0.02 -Note "6419/1819 (Techo)"

# ----------------------------------------------------------
# §7 Marco B Capa 1
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §7 Marco B Capa 1 ---"
Check -Id "MB1-500" -Computed (4474 / 500) -Reported 8.9 -Tolerance 0.1
Check -Id "MB1-750" -Computed (4474 / 750) -Reported 6.0 -Tolerance 0.1
Check -Id "MB1-1000" -Computed (4474 / 1000) -Reported 4.5 -Tolerance 0.1
Check -Id "MB1-2000" -Computed (4474 / 2000) -Reported 2.2 -Tolerance 0.1
Check -Id "MB1-2884" -Computed (4474 / 2884) -Reported 1.55 -Tolerance 0.02
Check -Id "MB1-354" -Computed (4474 / 354) -Reported 12.6 -Tolerance 0.1
Check -Id "MB1-62" -Computed (4474 / 62) -Reported 72.2 -Tolerance 0.1
Check -Id "MB1-6" -Computed (4474 / 6) -Reported 745.7 -Tolerance 0.5
Check -Id "MB1-2" -Computed (4474 / 2) -Reported 2237 -Tolerance 1

# ----------------------------------------------------------
# §7 Marco B Capa 2
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §7 Marco B Capa 2 ---"
$fd_pcts = @(0.089, 0.15, 0.42, 0.615)
$fd_names = @('8.9%', '15%', '42%', '61.5%')
$fd_rep_ratio = @(0.53, 0.89, 2.51, 3.67)
$fd_rep_med = @(398, 671, 1879, 2752)

for ($i = 0; $i -lt 4; $i++) {
    $med = 4474 * $fd_pcts[$i]
    $ratio = $med / 750
    Check -Id "MB2-MED-$($fd_names[$i])" -Computed $med -Reported $fd_rep_med[$i] -Tolerance 2 -Note "medidas injustificadas"
    Check -Id "MB2-RATIO-$($fd_names[$i])" -Computed $ratio -Reported $fd_rep_ratio[$i] -Tolerance 0.02 -Note "ratio /750"
}

# Tabla sensibilidad
Write-Output ""
Write-Output "--- §7 Tabla sensibilidad Capa 2 ---"
$sens_cond = @(2000, 1000, 750, 500)
$sens_cond_names = @('>2000', '1000', '750', '500')
$sens_expected = @(
    @(0.20, 0.40, 0.53, 0.80),   # 8.9%
    @(0.34, 0.67, 0.89, 1.34),   # 15%
    @(0.94, 1.88, 2.51, 3.76),   # 42%
    @(1.38, 2.75, 3.67, 5.50)    # 61.5%
)
for ($f = 0; $f -lt 4; $f++) {
    for ($c = 0; $c -lt 4; $c++) {
        $calc = (4474 * $fd_pcts[$f]) / $sens_cond[$c]
        Check -Id "SENS-$($fd_names[$f])-$($sens_cond_names[$c])" -Computed $calc -Reported $sens_expected[$f][$c] -Tolerance 0.02 -Note "$($fd_names[$f])/$($sens_cond_names[$c])"
    }
}

# ----------------------------------------------------------
# §7 Capa 3 NNyA afectados
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §7 Capa 3 NNyA ---"
$cap3_reported = @(557, 939, 2631, 3853)
for ($i = 0; $i -lt 4; $i++) {
    $nnya = 4474 * $fd_pcts[$i] * 1.4
    Check -Id "CAP3-$($fd_names[$i])" -Computed $nnya -Reported $cap3_reported[$i] -Tolerance 1.5 -Note "4474*$($fd_names[$i])*1.4"
}

# ----------------------------------------------------------
# §7 Capa 4 Extrapolacion
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §7 Capa 4 Extrapolacion x15 ---"
Check -Id "CAP4-MEDIDAS" -Computed (4474 * 15) -Reported 67000 -Tolerance 1000 -Note "4474*15"
Check -Id "CAP4-MA" -Computed (2.27 * 15) -Reported 34 -Tolerance 2 -Note "2.27*15 Marco A Restriccion"
Check -Id "CAP4-MB1" -Computed ((4474/750) * 15) -Reported 89 -Tolerance 2 -Note "6.0*15 Marco B1"
Check -Id "CAP4-089FD" -Computed (0.53 * 15) -Reported 7.9 -Tolerance 0.2 -Note "0.53*15"
Check -Id "CAP4-615FD" -Computed (3.67 * 15) -Reported 55 -Tolerance 1 -Note "3.67*15"
Check -Id "CAP4-DANO89" -Computed (557 * 15) -Reported 8300 -Tolerance 100 -Note "557*15"
Check -Id "CAP4-DANO615" -Computed (3853 * 15) -Reported 57500 -Tolerance 300 -Note "3853*15"

# ----------------------------------------------------------
# §14 Marco A Cordoba — provincial
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §14 Marco A Cordoba provincial ---"
Check -Id "CBA-A" -Computed (1107 / 977) -Reported 1.13 -Tolerance 0.02 -Note "1107/977 Escenario A (sin filtro)"
Check -Id "CBA-B-DENOM" -Computed (977 * 0.7255) -Reported 709 -Tolerance 1.5 -Note "977*72.55% denominador proxy UNQ"
Check -Id "CBA-B" -Computed (1107 / 709) -Reported 1.56 -Tolerance 0.02 -Note "1107/709 Escenario B (proxy etario)"
Check -Id "CBA-C-DENOM" -Computed (977 * 0.6151) -Reported 601 -Tolerance 1.5 -Note "977*61.51% denominador sobre total"
Check -Id "CBA-C" -Computed (1107 / 601) -Reported 1.84 -Tolerance 0.02 -Note "1107/601 Escenario C (sobre total)"

# ----------------------------------------------------------
# §14.9 Inconsistencia sub-provincial (audit, no ratio)
# ----------------------------------------------------------
Write-Output ""
Write-Output "--- §14.9 Inconsistencia SNIC departamental ---"
Check -Id "CBA-CAP-2020" -Computed 9 -Reported 9 -Tolerance 0 -Note "Capital DIS hechos 2020 (SNIC departamental)"
Check -Id "CBA-INT-2020" -Computed 968 -Reported 968 -Tolerance 0 -Note "Interior DIS hechos 2020 (SNIC departamental)"
Check -Id "CBA-TOTAL-2020" -Computed (9 + 968) -Reported 977 -Tolerance 0 -Note "9+968=977 coincide con CSV provincial"
Check -Id "CBA-CAP-2015" -Computed 1296 -Reported 1296 -Tolerance 0 -Note "Capital DIS hechos 2015 (pre-colapso)"
Check -Id "CBA-CAP-2016" -Computed 3 -Reported 3 -Tolerance 0 -Note "Capital DIS hechos 2016 (post-colapso)"
Check -Id "CBA-CAP-DROP" -Computed ([math]::Round((1296 - 3) / 1296 * 100, 1)) -Reported 99.8 -Tolerance 0.1 -Note "caida interanual Capital 2015->2016 (99.77%)"
Check -Id "CBA-MPF-GAP" -Computed ([math]::Round(2293 / 4, 0)) -Reported 573 -Tolerance 1 -Note "brecha MPF sumarios (2293) vs SNIC hechos (4) Capital 2018"

# ==========================================================
# RESUMEN
# ==========================================================
Write-Output ""
Write-Output "============================================================"
Write-Output " RESUMEN: PASS=$script:pass FAIL=$script:fail WARN=$script:warnings"
Write-Output "============================================================"
if ($script:fail -gt 0) {
    Write-Output " ACCION REQUERIDA: revisar items FAIL antes de publicar"
    exit 1
} else {
    Write-Output " Todas las cadenas aritmeticas verificadas"
    exit 0
}
