
function renderChart(){
var elem = document.getElementById("label_option");
var strTarget = elem.options[elem.selectedIndex].text;
 var div = document.getElementById('container-chart');
 $.ajax({
        url : '/generate?target='+strTarget,
                   type : 'GET',
                   success: function(data){
                       div.style.display="block";
                       constructChart(data)
                       }
                   });
}

function renderTable(){
var div_preview = document.getElementById('container-preview');

$('#form-target').css('display','none');
$('#container-chart').css('display','none');
div_preview.innerHTML=""
 $.ajax({
               url : '/preview',
               type : 'GET',
               success: function(data){
                 div_preview.innerHTML += data;
                 var table= div_preview.firstChild;
                 div_preview.style.display = "block";
                 constructTargetForm();
               },
               error: function(error){
                div_preview.innerHTML += "<h2> Cannot display preview </h2>";
                console.log(error);

               }

        });
}

function uploadFile()
{
var formData = new FormData();
formData.append('file', $('#file')[0].files[0]);
        $.ajax({
               url : '/upload',
               type : 'POST',
               data : formData,
               processData: false,
               contentType: false,
               success : function(response) {

                 renderTable();
               },
               error: function(error) {
                 console.log(error);
               }
        });
}


function constructChart(json_touple_array) {
    label_array=[]
    values_array=[]
    bedford_array=[]
    const myArray= JSON.parse(json_touple_array);
    for(var i=1; i<10; i++)
    {
        label_array.push(myArray[i][0]);
        values_array.push(myArray[i][1]);
        bedford_array.push(Math.log10(1+1/i)*100)
    }

  $('#chart').remove();
  $('#chart_content').append('<canvas id="chart"><canvas>');
  var canvas = document.getElementById('chart');
  var context = canvas.getContext("2d");

  var chart = new Chart(context, {
    data: {
        datasets: [{
            type: 'bar',
            label: 'Detected values',
            data: values_array,
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)'
        }, {
            type: 'line',
            label: "Bedford's law",
            data: bedford_array,
            fill: false,
            borderColor: 'rgb(54, 162, 235)'
        }],
        labels: label_array
    }
});
}

function constructTargetForm(){
var div = document.getElementById('form-target');
var dropdown = document.getElementById('label_option');
dropdown.innerHTML=""
 $.ajax({
        url : '/header',
        type : 'GET',
        success: function(data){
          const headerArray= JSON.parse(data);
          div.style.display="block";
          console.log(headerArray)
          $.each(headerArray, function(item){
                 dropdown.innerHTML +="  <option value="+headerArray[item]+">"+headerArray[item]+"</option>"
          });
         }
      });
}
