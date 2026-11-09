from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ohio S.B. 396 Leave Calculator</title>
  <style>
    :root { color-scheme: light; font-family: "Segoe UI", sans-serif; }
    body {
      min-height: 100vh;
      margin: 0;
      display: grid;
      place-items: start center;
      background: #f2f6f4;
      color: #172b27;
    }
    main {
      box-sizing: border-box;
      width: 100%;
      min-height: 100vh;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    h1 { margin: 0 0 1.5rem; font-size: 2.5rem; line-height: 1.15; }
    
    h2 { margin: 0 0 1.5rem; font-size: 1.5rem; line-height: 1.3; }

    .choices { display: flex; flex-wrap: wrap; justify-content: center; gap: 6.75rem; }
    .results {
      width: min(100%, 70rem);
      margin-top: auto;
      padding-top: 3rem;
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 1rem;
    }
    .result-box {
      min-height: 8rem;
      padding: 1.25rem 1rem;
      border: 1px solid #c9d6d1;
      border-radius: 6px;
      background: #fff;
      display: grid;
      place-items: start center;
    }
    .result-box h3 { margin: 0; font-size: 1.125rem; line-height: 1.3; }
    @media (max-width: 700px) {
      .results { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    .result-box h4 { margin: 0; font-size: 1.5rem; line-height: 1.3; }
        @media (max-width: 700px) {
      .results { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    button {
      min-width: 9rem;
      padding: 0.85rem 1.25rem;
      border: 1px solid #176b58;
      border-radius: 6px;
      background: #176b58;
      color: white;
      font: inherit;
      font-weight: 600;
      cursor: pointer;
    }
    button:hover { background: #105544; }
    button:focus-visible { outline: 3px solid #e6a23c; outline-offset: 3px; }
  </style>
</head>
<body>
  <main>
    <h1>Ohio S.B. 396 Leave Calculator</h1>
    <h2>Choose your pay type:</h2>
    <div class="choices">
      <button type="button" id = "hourly-button" onclick = "ChangePayType('hourly')">Hourly</button>
      <button type="button" id = "monthly-button" onclick = "ChangePayType('monthly')">Monthly</button>
      <button type="button" id = "salary-button" onclick = "ChangePayType('salary')">Salary</button>
    </div>

    <section class="results" aria-label="Benefit estimates">
      <article class="result-box"><h3>Annual Tax Cost</h3><h4><span id = "annual tax cost"></span></h4></article>
      <article class="result-box"><h3>Top Weeks of Benefit Available</h3><h4><span id = "Top Weeks of Benefit Available"></span></h4></article>
      <article class="result-box"><h3>Weekly Benefit</h3><h4><span id = "weekly benefit"></span></h4></article>
      <article class="result-box"><h3>Total Benefit Available.</h3><h4><span id = "total benefit available"></span></h4></article>
    </section>

      <div>
        <input type="range" min="0" max="100" value="0"
              class="myslider" id="sliderRange">
        <p>
        <span id = "Hours Worked"></span> 
        <span id="demo"></span>
        </p>
      </div>





      <div>
        <input type="range" min="0" max="100" value="0"
              class="myslider" id="sliderRange2">
        <p>
        <span id = "Hourly Wage"></span> 
        <span id="demo2"></span>
        </p>
      </div>
      <div>
        <input type="range" min="0" max="20000" value="0"
              class="myslider" id="sliderRange3">
        <p>
        <span id = "Monthly Salary"></span> 
        <span id="demo3"></span>
        </p>
      </div>
      <div>
        <input type="range" min="0" max="250000" value="0"
              class="myslider" id="sliderRange4">
        <p>
        <span id = "Annual Salary"></span>
        <span id="demo4"></span>
        </p>
      </div>








      <script>
        // Pointer variable to track the selected pay type
        var pointer = 0;

        // Set the text content of the spans to describe the sliders
        document.getElementById("Hours Worked").textContent = "Hours Worked:";
        document.getElementById("Hourly Wage").textContent = "Hourly Wage:";
        document.getElementById("Monthly Salary").textContent = "Monthly Salary:";
        document.getElementById("Annual Salary").textContent = "Annual Salary:";

        function ChangePayType(payType) {
          let hourlyButton = document.getElementById("hourly-button");
          let monthlyButton = document.getElementById("monthly-button");
          let salaryButton = document.getElementById("salary-button");

          // Reset all buttons to default state
          hourlyButton.style.backgroundColor = "#176b58";
          monthlyButton.style.backgroundColor = "#176b58";
          salaryButton.style.backgroundColor = "#176b58";

          // Highlight the selected button
          if (payType === "hourly") {
            hourlyButton.style.backgroundColor = "#105544";
          } else if (payType === "monthly") {
            monthlyButton.style.backgroundColor = "#105544";
          } else if (payType === "salary") {
            salaryButton.style.backgroundColor = "#105544";
          }



          if (payType === "hourly") {
            // Show the hourly slider and hide others
            document.getElementById("sliderRange").style.display = "block";
            document.getElementById("sliderRange2").style.display = "block";
            document.getElementById("sliderRange3").style.display = "none";
            document.getElementById("sliderRange4").style.display = "none";

            document.getElementById("Hours Worked").style.display = "block";
            document.getElementById("Hourly Wage").style.display = "block";
            document.getElementById("Monthly Salary").style.display = "none";
            document.getElementById("Annual Salary").style.display = "none";

            document.getElementById("demo").style.display = "block";
            document.getElementById("demo2").style.display = "block";
            document.getElementById("demo3").style.display = "none";
            document.getElementById("demo4").style.display = "none";

          } else if (payType === "monthly") {
            // Show the monthly slider and hide others
            document.getElementById("sliderRange").style.display = "none";
            document.getElementById("sliderRange2").style.display = "none";
            document.getElementById("sliderRange3").style.display = "block";
            document.getElementById("sliderRange4").style.display = "none";

            document.getElementById("Hours Worked").style.display = "none";
            document.getElementById("Hourly Wage").style.display = "none";
            document.getElementById("Monthly Salary").style.display = "block";
            document.getElementById("Annual Salary").style.display = "none";

            document.getElementById("demo").style.display = "none";
            document.getElementById("demo2").style.display = "none";
            document.getElementById("demo3").style.display = "block";
            document.getElementById("demo4").style.display = "none";

          } else if (payType === "salary") {
            // Show the salary slider and hide others
            document.getElementById("sliderRange").style.display = "none";
            document.getElementById("sliderRange2").style.display = "none";
            document.getElementById("sliderRange3").style.display = "none";
            document.getElementById("sliderRange4").style.display = "block";

            document.getElementById("Hours Worked").style.display = "none";
            document.getElementById("Hourly Wage").style.display = "none";
            document.getElementById("Monthly Salary").style.display = "none";
            document.getElementById("Annual Salary").style.display = "block";

            document.getElementById("demo").style.display = "none";
            document.getElementById("demo2").style.display = "none";
            document.getElementById("demo3").style.display = "none";
            document.getElementById("demo4").style.display = "block";
          }

          // Controlling Pointers
          if (payType === "hourly") {
            pointer = 1;
          } else if (payType === "monthly") {
            pointer = 2;
          } else if (payType === "salary") {
            pointer = 3;
          }


        }

        // Default Variable Values
        if (pointer === 0) {
          let uservalue = document.getElementById("annual tax cost");
          let uservalue2 = document.getElementById("Top Weeks of Benefit Available");
          let uservalue3 = document.getElementById("weekly benefit");
          let uservalue4 = document.getElementById("total benefit available");

          let taxvalue = 0;
          let topweeksvalue = 14;
          let weeklybenefitvalue = 0;
          let totalbenefitvalue = 0;

          taxvalue = parseFloat(taxvalue).toFixed(2);
          topweeksvalue = parseFloat(topweeksvalue).toFixed(2);
          weeklybenefitvalue = parseFloat(weeklybenefitvalue).toFixed(2);
          totalbenefitvalue = parseFloat(totalbenefitvalue).toFixed(2);

          uservalue.textContent = taxvalue;
          uservalue2.textContent = topweeksvalue;
          uservalue3.textContent = weeklybenefitvalue;
          uservalue4.textContent = totalbenefitvalue;
        }


        let slider = document.getElementById("sliderRange");
        let output = document.getElementById("demo");

        // Update variable and display on every slider movement
        slider.addEventListener("input", function () {
          let value = this.value; // continuously updating variable
          output.textContent = value; // update the page

          let uservalue = document.getElementById("annual tax cost");
          let uservalue2 = document.getElementById("Top Weeks of Benefit Available");
          let uservalue3 = document.getElementById("weekly benefit");
          let uservalue4 = document.getElementById("total benefit available");

          let taxvalue = output.textContent * output2.textContent * 52 * 0.04;
          let topweeksvalue = 14;

          let weeklybenefitvalue;
          if (output.textContent * output2.textContent * 0.85 <= 1153) {
          weeklybenefitvalue = output.textContent * output2.textContent * 0.85;
          } 
          else {
          weeklybenefitvalue = 1153;
          }

          let totalbenefitvalue = weeklybenefitvalue * topweeksvalue;

          taxvalue = parseFloat(taxvalue).toFixed(2);
          topweeksvalue = parseFloat(topweeksvalue).toFixed(2);
          weeklybenefitvalue = parseFloat(weeklybenefitvalue).toFixed(2);
          totalbenefitvalue = parseFloat(totalbenefitvalue).toFixed(2);

          uservalue.textContent = taxvalue;
          uservalue2.textContent = topweeksvalue;
          uservalue3.textContent = weeklybenefitvalue;
          uservalue4.textContent = totalbenefitvalue;
        });





        let slider2 = document.getElementById("sliderRange2");
        let output2 = document.getElementById("demo2");

        // Update variable and display on every slider movement
        slider2.addEventListener("input", function () {
          let value = this.value; // continuously updating variable
          output2.textContent = value; // update the page

          let uservalue = document.getElementById("annual tax cost");
          let uservalue2 = document.getElementById("Top Weeks of Benefit Available");
          let uservalue3 = document.getElementById("weekly benefit");
          let uservalue4 = document.getElementById("total benefit available");

          let taxvalue = output.textContent * output2.textContent * 52 * 0.004;
          let topweeksvalue = 14;

          let weeklybenefitvalue;
          if (output.textContent * output2.textContent * 0.85 <= 1153) {
          weeklybenefitvalue = output.textContent * output2.textContent * 0.85;
          } 
          else {
          weeklybenefitvalue = 1153;
          }
          let totalbenefitvalue = weeklybenefitvalue * topweeksvalue;

          taxvalue = parseFloat(taxvalue).toFixed(2);
          topweeksvalue = parseFloat(topweeksvalue).toFixed(2);
          weeklybenefitvalue = parseFloat(weeklybenefitvalue).toFixed(2);
          totalbenefitvalue = parseFloat(totalbenefitvalue).toFixed(2);

          uservalue.textContent = taxvalue;
          uservalue2.textContent = topweeksvalue;
          uservalue3.textContent = weeklybenefitvalue;
          uservalue4.textContent = totalbenefitvalue;
        });




        let slider3 = document.getElementById("sliderRange3");
        let output3 = document.getElementById("demo3");

        // Update variable and display on every slider movement
        slider3.addEventListener("input", function () {
          let value = this.value; // continuously updating variable
          output3.textContent = value; // update the page

          
          let uservalue = document.getElementById("annual tax cost");
          let uservalue2 = document.getElementById("Top Weeks of Benefit Available");
          let uservalue3 = document.getElementById("weekly benefit");
          let uservalue4 = document.getElementById("total benefit available");

          let taxvalue = output3.textContent * 12 * 0.004;
          let topweeksvalue = 14;

          let weeklybenefitvalue;
          if (output3.textContent *12 /52 * 0.85 <= 1153) {
          weeklybenefitvalue = output3.textContent *12 /52 * 0.85;
          } 
          else {
          weeklybenefitvalue = 1153;
          }
          let totalbenefitvalue = weeklybenefitvalue * topweeksvalue;

          taxvalue = parseFloat(taxvalue).toFixed(2);
          topweeksvalue = parseFloat(topweeksvalue).toFixed(2);
          weeklybenefitvalue = parseFloat(weeklybenefitvalue).toFixed(2);
          totalbenefitvalue = parseFloat(totalbenefitvalue).toFixed(2);

          uservalue.textContent = taxvalue;
          uservalue2.textContent = topweeksvalue;
          uservalue3.textContent = weeklybenefitvalue;
          uservalue4.textContent = totalbenefitvalue;
        });




        let slider4 = document.getElementById("sliderRange4");
        let output4 = document.getElementById("demo4");

        // Update variable and display on every slider movement
        slider4.addEventListener("input", function () {
          let value = this.value; // continuously updating variable
          output4.textContent = value; // update the page

          
          let uservalue = document.getElementById("annual tax cost");
          let uservalue2 = document.getElementById("Top Weeks of Benefit Available");
          let uservalue3 = document.getElementById("weekly benefit");
          let uservalue4 = document.getElementById("total benefit available");

          let taxvalue = output4.textContent * 0.004;
          let topweeksvalue = 14;
    
          let weeklybenefitvalue;
          if (output4.textContent /52 * 0.85 <= 1153) {
          weeklybenefitvalue = output4.textContent /52 * 0.85;
          } 
          else {
          weeklybenefitvalue = 1153;
          }

          let totalbenefitvalue = weeklybenefitvalue * topweeksvalue;

          taxvalue = parseFloat(taxvalue).toFixed(2);
          topweeksvalue = parseFloat(topweeksvalue).toFixed(2);
          weeklybenefitvalue = parseFloat(weeklybenefitvalue).toFixed(2);
          totalbenefitvalue = parseFloat(totalbenefitvalue).toFixed(2);

          uservalue.textContent = taxvalue;
          uservalue2.textContent = topweeksvalue;
          uservalue3.textContent = weeklybenefitvalue;
          uservalue4.textContent = totalbenefitvalue;

        });


      </script>
  </main>
</body>
</html>
"""


class PageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), PageHandler)
    print("Serving at http://127.0.0.1:8000")
    server.serve_forever()
