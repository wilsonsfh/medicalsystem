{% extends 'layout.html' %}
{% block body %}

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<link rel="stylesheet" type="text/css" href="/static/css/appointment.css">
<div class="jumbotron">
  <div class="container text-center">
      <div id="head">
   <h1>{{ title }}</h1>
          </div>

    <div id="head-p"> <p> Doctor Opening Hours Slot  </p> </div>

  </div>
</div>



  <div class="panel-group">
    <div class="panel panel-default">
      <div class="panel-heading"> <h3> Doctor Admin Page </h3> </div>
    <div id="appointment_box">


    </div>


    <form>
    <table class="table table-bordered">
        <thead>
        <tr>
                <th> Monday  </th>
                <td id="m1" style="background-color:lightgrey"> {{dform.active (id="m1")}} 8 : 00 </td>
                <td id="m2" style="background-color:lightgrey"> {{dform.active (id="m2")}} 9 : 00</td>
                <td id="m3" style="background-color:lightgrey"> {{dform.active (id="m3") }} 10 : 00 </td>
                <td id="m4" style="background-color:lightgrey"> {{dform.active (id="m4")}} 11 : 00</td>
                <td id="m5" style="background-color:lightgrey"> {{dform.active (id="m5")}} 12 : 00</td>
                <td id="m6" style="background-color:lightgrey"> {{dform.active (id="m6")}} 13 : 00</td>
                <td id="m7" style="background-color:lightgrey"> {{dform.active (id="m7")}} 14 : 00</td>
                <td id="m8" style="background-color:lightgrey"> {{dform.active (id="m8")}} 15 : 00</td>
                <td id="m9" style="background-color:lightgrey"> {{dform.active}} 16 : 00</td>
                <td id="m10" style="background-color:lightgrey"> {{dform.active}} 17 : 00</td>
                <td id="m12" style="background-color:lightgrey"> {{dform.active}} 18 : 00</td>
        </tr>

<tr>
                  <th> Tuesday </th>
                <td id="t1" style="background-color:lightgrey"> {{dform.active}} 8 : 00 </td>
                <td id="t2" style="background-color:lightgrey"> {{dform.active}} 9 : 00</td>
                <td id="t3" style="background-color:lightgrey"> {{dform.active}} 10 : 00 </td>
                <td id="t4" style="background-color:lightgrey"> {{dform.active}} 11 : 00</td>
                <td id="t5" style="background-color:lightgrey"> {{dform.active}} 12 : 00</td>
                <td id="t6" style="background-color:lightgrey"> {{dform.active}} 13 : 00</td>
                <td id="t7" style="background-color:lightgrey"> {{dform.active}} 14 : 00</td>
                <td id="t8" style="background-color:lightgrey"> {{dform.active}} 15 : 00</td>
                <td id="t9" style="background-color:lightgrey"> {{dform.active}} 16 : 00</td>
                <td id="t10" style="background-color:lightgrey"> {{dform.active}} 17 : 00</td>
                <td id="t11" style="background-color:lightgrey"> {{dform.active}} 18 : 00</td>
        </tr>

        <tr>
                          <th> Wednesday </th>
                <td id="w1" style="background-color:lightgrey"> {{dform.active}} 8 : 00 </td>
                <td id="w2" style="background-color:lightgrey"> {{dform.active}} 9 : 00</td>
                <td id="w3" style="background-color:lightgrey"> {{dform.active}} 10 : 00 </td>
                <td id="w4" style="background-color:lightgrey"> {{dform.active}} 11 : 00</td>
                <td id="w5" style="background-color:lightgrey"> {{dform.active}} 12 : 00</td>
                <td id="w6" style="background-color:lightgrey"> {{dform.active}} 13 : 00</td>
                <td id="w7" style="background-color:lightgrey"> {{dform.active}} 14 : 00</td>
                <td id="w8" style="background-color:lightgrey"> {{dform.active}} 15 : 00</td>
                <td id="w9" style="background-color:lightgrey"> {{dform.active}} 16 : 00</td>
                <td id="w10" style="background-color:lightgrey"> {{dform.active}} 17 : 00</td>
                <td id="w11" style="background-color:lightgrey"> {{dform.active}} 18 : 00</td>
        </tr>
                <tr>
                          <th> Thursday </th>
                <td id="th1" style="background-color:lightgrey"> {{dform.active}} 8 : 00 </td>
                <td id="th2" style="background-color:lightgrey"> {{dform.active}} 9 : 00</td>
                <td id="th3" style="background-color:lightgrey"> {{dform.active}} 10 : 00 </td>
                <td id="th4" style="background-color:lightgrey"> {{dform.active}} 11 : 00</td>
                <td id="th5" style="background-color:lightgrey"> {{dform.active}} 12 : 00</td>
                <td id="th6" style="background-color:lightgrey"> {{dform.active}} 13 : 00</td>
                <td id="th7" style="background-color:lightgrey"> {{dform.active}} 14 : 00</td>
                <td id="th8" style="background-color:lightgrey"> {{dform.active}} 15 : 00</td>
                <td id="th9" style="background-color:lightgrey"> {{dform.active}} 16 : 00</td>
                <td id="th10" style="background-color:lightgrey"> {{dform.active}} 17 : 00</td>
                <td id="th11" style="background-color:lightgrey"> {{dform.active}} 18 : 00</td>
        </tr>


                <tr>
                          <th> Friday </th>
                <td id="f1"  style="background-color:lightgrey"> {{dform.active}} 8 : 00 </td>
                <td id="f2"  style="background-color:lightgrey"> {{dform.active}} 9 : 00</td>
                <td id="f3"  style="background-color:lightgrey"> {{dform.active}} 10 : 00 </td>
                <td id="f4"  style="background-color:lightgrey"> {{dform.active}} 11 : 00</td>
                <td id="f5"  style="background-color:lightgrey"> {{dform.active}} 12 : 00</td>
                <td id="f6"  style="background-color:lightgrey"> {{dform.active}} 13 : 00</td>
                <td id="f7"  style="background-color:lightgrey"> {{dform.active}} 14 : 00</td>
                <td id="f8"  style="background-color:lightgrey"> {{dform.active}} 15 : 00</td>
                <td id="f9"  style="background-color:lightgrey"> {{dform.active}} 16 : 00</td>
                <td id="f10" style="background-color:lightgrey"> {{dform.active}} 17 : 00</td>
                <td id="f11" style="background-color:lightgrey"> {{dform.active}} 18 : 00</td>
        </tr>

                <tr>
                          <th> Saturday </th>
                <td id="s1" style="background-color:lightgrey"> {{dform.active}} 8 : 00 </td>
                <td id="s2" style="background-color:lightgrey"> {{dform.active}} 9 : 00</td>
                <td id="s3" style="background-color:lightgrey"> {{dform.active}} 10 : 00 </td>
                <td id="s4" style="background-color:lightgrey"> {{dform.active}} 11 : 00</td>
                <td id="s5" style="background-color:lightgrey"> {{dform.active}} 12 : 00</td>
                <td id="s6" style="background-color:lightgrey"> {{dform.active}} 13 : 00</td>
                <td id="s7" style="background-color:lightgrey"> {{dform.active}} 14 : 00</td>
                <td id="s8" style="background-color:lightgrey"> {{dform.active}} 15 : 00</td>
                <td id="s9" style="background-color:lightgrey"> {{dform.active}} 16 : 00</td>
                <td id="s10" style="background-color:lightgrey"> {{dform.active}} 17 : 00</td>
                <td id="s11" style="background-color:lightgrey"> {{dform.active}} 18 : 00</td>
        </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
  <br>
         <div class="form-group">
            <div class="form-row">
                <div class="form-group col-md-11">


                </div>
                <div class="form-group col-md-1">
                    <input type="submit" value="Submit" class="btn btn-info"/>
                </div>
            </div>
        </div>

    </form>

    </div>
  </div>

{% endblock %}
