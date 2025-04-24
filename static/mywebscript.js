let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            document.getElementById("system_response").innerHTML = response.emotion_result;
        }
    };

    // Open a POST request to the emotionDetector endpoint
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    // Send the input text as a JSON object
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
};