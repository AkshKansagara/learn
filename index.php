<!DOCTYPE html>
<html>
<head>
    <title>Round Robin Scheduling</title>
    <style>
        table {
            border-collapse: collapse;
            width: 60%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        .gantt-chart {
            width: 90%;
            margin: 20px auto;
            border: 1px solid #ddd;
            position: relative;
            padding: 10px;
        }
        .process-bar {
            display: inline-block;
            background-color: #007bff;
            color: white;
            padding: 5px;
            border-radius: 5px;
            position: absolute;
            text-align: center;
        }
        h2{
            color: aqua;
        }
    </style>
</head>
<body>

<h2>Round Robin Scheduling</h2>

<form method="post">
    <label for="processes">Enter Processes:</label>
    <input type="text" id="processes" name="processes" placeholder="e.g., P1,P2,P3">
    <br><br>
    <label for="arrival_times">Enter Arrival Times:</label>
    <input type="text" id="arrival_times" name="arrival_times" placeholder="e.g., 0,1,2">
    <br><br>
    <label for="burst_times">Enter Burst Times:</label>
    <input type="text" id="burst_times" name="burst_times" placeholder="e.g., 5,3,8">
    <br><br>
    <label for="quantum">Enter Time Quantum:</label>
    <input type="text" id="quantum" name="quantum" placeholder="e.g., 2">
    <br><br>
    <input type="submit" value="Submit">
</form>

<?php
function roundRobin($processes, $burstTimes, $arrivalTimes, $quantum) {
    $n = count($processes);
    $remainingTime = $burstTimes;
    $completionTime = array_fill(0, $n, 0);
    $waitingTime = array_fill(0, $n, 0);
    $turnAroundTime = array_fill(0, $n, 0);
    $currentTime = 0;
    $ganttChart = "";
    while (true) {
        $done = true;
        for ($i = 0; $i < $n; $i++) {
            if ($remainingTime[$i] > 0 && $arrivalTimes[$i] <= $currentTime) {
                $done = false;
                if ($remainingTime[$i] > $quantum) {
                    $currentTime += $quantum;
                    $remainingTime[$i] -= $quantum;
                    $ganttChart .= "<div class='process-bar'>{$processes[$i]}</div>";
                } else {
                    $currentTime += $remainingTime[$i];
                    $completionTime[$i] = $currentTime;
                    $waitingTime[$i] = $currentTime - $burstTimes[$i] - $arrivalTimes[$i];
                    $remainingTime[$i] = 0;
                    $ganttChart .= "<div class='process-bar'>{$processes[$i]}</div>";
                }
            }
        }
        if ($done === true) {
            $minArrivalTime = min($arrivalTimes);
            $currentTime = $minArrivalTime;
            if ($done === true && max($remainingTime) == 0) {
                break;
            }
        }
    }
    for ($i = 0; $i < $n; $i++) {
        $turnAroundTime[$i] = $completionTime[$i] - $arrivalTimes[$i];
    }
    // echo "<h3>Schedule Result:</h3>";
    // echo "<div class='gantt-chart'>$ganttChart</div>";
    echo "<table>";
    echo "<tr><th>Process</th><th>Arrival Time</th><th>Burst Time</th><th>Completion Time</th><th>Turnaround Time</th><th>Waiting Time</th></tr>";
    $totalTAT = 0;
    $totalWT = 0;
    for ($i = 0; $i < $n; $i++) {
        echo "<tr><td>{$processes[$i]}</td><td>{$arrivalTimes[$i]}</td><td>{$burstTimes[$i]}</td><td>{$completionTime[$i]}</td><td>{$turnAroundTime[$i]}</td><td>{$waitingTime[$i]}</td></tr>";
        $totalTAT += $turnAroundTime[$i];
        $totalWT += $waitingTime[$i];
    }
    echo "</table>";
    $avgTAT = $totalTAT / $n;
    $avgWT = $totalWT / $n;
    echo "<p>Average Turnaround Time: $avgTAT</p>";
    echo "<p>Average Waiting Time: $avgWT</p>";
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $processes = explode(",", $_POST["processes"]);
    $burstTimes = explode(",", $_POST["burst_times"]);
    $arrivalTimes = explode(",", $_POST["arrival_times"]);
    $quantum = intval($_POST["quantum"]);

    roundRobin($processes, $burstTimes, $arrivalTimes, $quantum);
}
?>
</body>
</html>