<?php
  $errorMessage = "";
  $successMessage = "";

  function checkExisting($conn, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail, $varComments) {
    $query_sql = $conn->query("SELECT count(*) FROM mailing_list_test WHERE " .
      "first_name = '" . $varFirstName . "' and " .
      "last_name = '" . $varLastName . "' and " .
      "job_title = '" . $varJobTitle . "' and " .
      "company = '" . $varCompany . "' and " .
      "address = '" . $varAddress . "' and " .
      "city = '" . $varCity . "' and " .
      "state = '" . $varState . "' and " .
      "zip_code = " . $varZip . " and " .
      "country = '" . $varCountry . "' and " .
      "email = '" . $varEmail . "' " .
      "limit 1");

      try {
        $results = $query_sql->fetchAll(PDO::FETCH_ASSOC);

        $count = (int)$results[0]["count(*)"];
        return($count);
      } catch(PDOException $e) {
        // echo "Error running query: " . $e->getMessage();
        echo "Error running query.";
      }
      return(999);
  }

  function removeEntry($varTable, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail) {
    $sql = "DELETE FROM " . $varTable . " WHERE " .
      "first_name = '" . $varFirstName . "' and " .
      "last_name = '" . $varLastName . "' and " .
      "job_title = '" . $varJobTitle . "' and " .
      "company = '" . $varCompany . "' and " .
      "address = '" . $varAddress . "' and " .
      "city = '" . $varCity . "' and " .
      "state = '" . $varState . "' and " .
      "zip_code = " . $varZip . " and " .
      "country = '" . $varCountry . "' and " .
      "email = '" . $varEmail . "' ";

    return($sql);
  }

  function addNewRow($varTable, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail, $varComments) {
        $sql = "INSERT INTO " . $varTable . " (first_name, last_name, job_title, company, address, city, state, zip_code, country, email, comments) VALUES (".
        "'" . $varFirstName . "', " .
        "'" . $varLastName . "', " .
        "'" . $varJobTitle . "', " .
        "'" . $varCompany . "', " .
        "'" . $varAddress . "', " .
        "'" . $varCity . "', " .
        "'" . $varState . "', " .
        $varZip . ", " .
        "'" . $varCountry . "', " .
        "'" . $varEmail . "', " .
        "'" . $varComments . "'" .
        ")";

      return($sql);
  }

  function decisionTree($conn, $varSubscribe, $varTable, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail, $varComments) {
    global $successMessage;
    $sql = "";
    $matching_rows_count = checkExisting($conn, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail, $varComments);

    if($varSubscribe == "add") {
      if($matching_rows_count < 1) {
        $sql = addNewRow($varTable, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail, $varComments);
        $successMessage .= "Information added successfully!";
      }
      else {
        // echo "Information already exists in database.<br>";
        global $errorMessage;
        $errorMessage .= "Information already exists in database.<br>";
      }
    } 
    elseif($varSubscribe == "remove") {
      if($matching_rows_count < 1) {
        // echo "Information does not exist in the database<br>";
        global $errorMessage;
        $errorMessage .= "Information does not exist in the database<br>";
      }
      else {
        $sql = removeEntry($varTable, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail);
        $successMessage .= "Information removed from our records successfully.";
      }
    }
      return($sql);
  }

	if($_POST['formSubmit'] == "Submit") 
    {
		// $errorMessage = "";
		
		if(empty($_POST['formFirstName'])) 
        {
			$errorMessage .= "<li>You forgot to enter your first name!</li>";
		}
    if(empty($_POST['formLastName'])) 
        {
      $errorMessage .= "<li>You forgot to enter your last name!</li>";
    }
		if(empty($_POST['formCompany'])) 
        {
			$errorMessage .= "<li>You forgot to enter your company!</li>";
		}
		if(empty($_POST['formAddress'])) 
        {
			$errorMessage .= "<li>You forgot to enter your address!</li>";
		}
		if(empty($_POST['formCity'])) 
        {
			$errorMessage .= "<li>You forgot to enter your city!</li>";
		}
		if(empty($_POST['formState'])) 
        {
			$errorMessage .= "<li>You forgot to enter state!</li>";
		}
		if(empty($_POST['formZip'])) 
        {
			$errorMessage .= "<li>You forgot to enter your ZIP code</li>";
		}
    if(empty($_POST['formCountry'])) 
        {
      $errorMessage .= "<li>You forgot to enter your Country</li>";
    }
		if(empty($_POST['formSubscribe'])) 
        {
			$errorMessage .= "<li>Subscribe to mailing list?</li>";
		}
    if(empty($_POST['6_letters_code']))
        {
      $errorMessage .= "<li>You must enter the 6 character security code";
    }

    $varFirstName = $_POST['formFirstName'];
    $varLastName = $_POST['formLastName'];
    $varJobTitle = $_POST['formJobTitle'];
    $varCompany = $_POST['formCompany'];
    $varAddress = $_POST['formAddress'];
    $varApartment = $_POST['formApartment'];
    $varCity = $_POST['formCity'];
    $varState = $_POST['formState'];
    $varZip = $_POST['formZip'];
    $varCountry = $_POST['formCountry'];
    $varEmail = $_POST['formEmail'];
    $varComments = $_POST['formComments'];
    $varSubscribe = $_POST['formSubscribe'];

    $servername = "db154.pair.com:3306";
    $username = "denevi_10_w";
    $password = "96rq8Wnr";
    $dbname = "denevi_arrow";
    $varTable = "mailing_list_test";


	if(empty($errorMessage)) {
		// Create a connection to the db
		try {
			$conn = new PDO("mysql:host=$servername; dbname=$dbname", $username, $password);
      
			// Set the PDO error mode to exception
			$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

      $sql = decisionTree($conn, $varSubscribe, $varTable, $varFirstName, $varLastName, $varJobTitle, $varCompany, $varAddress, $varCity, $varState, $varZip, $varCountry, $varEmail, $varComments);

			// Use exec() because no results are returned
      if ($sql != "") {
        $conn->exec($sql);
      }
			
			//header("Location: /thankyou.html");
			//exit();
		} catch(PDOException $e) {
			echo "Error communicating with database: " . $e->getMessage();
      // echo "<br>Using the following values:<br>";
      // echo $varFirstName . "<br>";
      // echo $varLastName . "<br>";
      // echo $varJobTitle . "<br>";
      // echo $varCompany . "<br>";
      // echo $varAddress . "<br>";
      // echo $varCity . "<br>";
      // echo $varState . "<br>";
      // echo $varZip . "<br>";
      // echo $varCountry . "<br>";
      // echo $varEmail . "<br>";
      // echo $varComments . "<br>";
		}

    $conn = null;
	}

  
            
    // function: PrepSQL()
    // use stripslashes and mysql_real_escape_string PHP functions
    // to sanitize a string for use in an SQL query
    //
    // also puts single quotes around the string
    //
    // function PrepSQL($value)
    // {
    //     // Stripslashes
    //     if(get_magic_quotes_gpc()) 
    //     {
    //         $value = stripslashes($value);
    //     }

    //     // Quote
    //     $value = "'" . mysql_real_escape_string($value) . "'";

    //     return($value);
    // }

    // $dbConn = null;
  }
?>






<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <title>Arrow | Linear Technology New Products Catalog Request
    </title>
    <!-- define some style elements-->
    <style>
      label,a 
      {
        font-family : Arial, Helvetica, sans-serif;
        font-size : 12px;
      }
      .clear {
        clear:both;
      }
      .header {
        width:80%;
        height:100px;
        background-color:#fff;
        border-bottom-left-radius:5px;
        border-bottom-right-radius:5px;
        border-top-left-radius:5px;
        border-top-right-radius:5px;
        margin-left:auto;
        margin-right:auto;
      }
      .footer {
        width:80%;
        height:30px;
      }
      .form {
        width:280px;
        padding:20px;
        border-color:#666;
        border-style:solid;
        border-width:thin;
        border-bottom-left-radius:5px;
        border-bottom-right-radius:5px;
        border-top-left-radius:5px;
        border-top-right-radius:5px;
        float:left;
        background-color:#fff;
      }
      .left {
        float:left;
        width:300px;
        padding-left:20px;
        padding-right:20px;
        height:auto;
      }
      .clear {
        clear:both;
      }
      #grad {
        background: white;
        /* For browsers that do not support gradients */
        background: -webkit-linear-gradient(#2f80b8, #86caf9);
        /* For Safari 5.1 to 6.0 */
        background: -o-linear-gradient(#2f80b8, #86caf9);
        /* For Opera 11.1 to 12.0 */
        background: -moz-linear-gradient(#2f80b8, #86caf9);
        /* For Firefox 3.6 to 15 */
        background: linear-gradient(#2f80b8, #86caf9);
        /* Standard syntax */
        max-width:100%;
      }
      .headertext {
        font-family:Segoe, "Segoe UI", "DejaVu Sans", "Trebuchet MS", Verdana, sans-serif;
        font-size:40px;
      }
      .subtext {
        font-family:Segoe, "Segoe UI", "DejaVu Sans", "Trebuchet MS", Verdana, sans-serif;
        font-size:14px;
        color:#fff;
      }
      .subtext-2 {
        font-family:Segoe, "Segoe UI", "DejaVu Sans", "Trebuchet MS", Verdana, sans-serif;
        font-size:11px;
        color:#fff;
      }
      .footertext {
        font-family:Segoe, "Segoe UI", "DejaVu Sans", "Trebuchet MS", Verdana, sans-serif;
        font-size:12px;
      }
    </style>  
  </head>
  <body>
    <div id="grad">
      <br />
      <br />
      <div class="header">&nbsp; &nbsp;
        <img src="/arrow-linear-header.jpg" height="100"/>
      </div>
      <br />
      <br />
      <div class="headertext" align="center"> 
        <strong>New Products Catalog Request
        </strong>
      </div>
      <br />
      <?php
        if(!empty($errorMessage)) 
        {
          echo("<div align='center'><p style='color:red; font-size:1.25em;'>There was an error with your form:</p>\n");
          echo("<ul style='color:red; font-size:1.25em;'>" . $errorMessage . "</ul></div>\n");
        }
      ?>
      <?php
        if(!empty($successMessage)) {
          echo("<div align='center'><p style='color:white; font-size:1.25em;'>" . $successMessage . "</p></div>\n");
        }
      ?>
      <div style="padding-left:auto; padding-right:auto;">
        <p>
        </p>
      </div>
      <div align="center">
        <table width="700" border="0" cellspacing="0" cellpadding="0">
          <form action="" method="post">
            <tr>
              <td width="20" height="100" valign="top">
                <input type="radio" name="formSubscribe" id="radio3" value="add">
              </td>
              <td width="321" valign="top">
                <span class="subtext">Yes, I would like to subscribe to the 
                  Arrow/Linear Technology quarterly catalog
                </span>
                <br />
                <br />
                <span class="subtext-2">
                  <i>Please fill out the form to the right to receive our latest catalog
                    <br />
                  </i>
                </span>
              </td>
              <td width="14" rowspan="2" valign="top">&nbsp;
              </td>
              <td width="14" rowspan="2" valign="top">&nbsp;
              </td>
              <td width="331" rowspan="2" valign="top">
                <div class="form">
                  <p>
                    <label for='formFirstName'>First Name</label>
                    <br/>
                    <input type="text" name="formFirstName" maxlength="50" value="<?=$varMovie;?>" />
                  </p>
                  <p>
                    <label for='formLastName'>Last Name</label>
                    <br/>
                    <input type="text" name="formLastName" maxlength="50" value="<?=$varMovie;?>" />
                  </p>
                  <p>
                    <label for='formJobTitle'>Title</label>
                    <br/>
                    <input type="text" name="formJobTitle" maxlength="50" value="<?=$varName;?>" />
                  </p>
                  <p>
                    <label for='formCompany'>Company</label>
                    <br/>
                    <input type="text" name="formCompany" maxlength="50" value="<?=$varName;?>" />
                  </p>
                  <p>
                    <label for='formAddress'>Street Address</label>
                    <br/>
                    <input type="text" name="formAddress" maxlength="50" value="<?=$varName;?>" />
                  </p>
                  <p>
                    <label for='formApartment'>Apartment/Suite/Building (optional)</label>
                    <br/>
                    <input type="text" name="formApartment" maxlength="50" value="<?=$varName;?>" />
                  </p>
                  <p>
                    <label for='formCity'>City</label>
                    <br/>
                    <input type="text" name="formCity" maxlength="50" value="<?=$varName;?>" />
                  </p>
                  <p>
                    <label for="formState">State</label>
                    <select name="formState">
                      <option value="">Select...
                      </option>
                      <option value="AL"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Alabama
                      </option>
                      <option value="AK"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Alaska
                      </option>
                      <option value="AZ"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Arizona
                      </option>
                      <option value="AR"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Arkansas
                      </option>
                      <option value="CA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>California
                      </option>
                      <option value="CO"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Colorado
                      </option>
                      <option value="CT"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Connecticut
                      </option>
                      <option value="DE"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Delaware
                      </option>
                      <option value="DC"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>District of Columbia
                      </option>
                      <option value="FL"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Florida
                      </option>
                      <option value="GA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Georgia
                      </option>
                      <option value="HI"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Hawaii
                      </option>
                      <option value="ID"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Idaho
                      </option>
                      <option value="IL"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Illinois
                      </option>
                      <option value="IN"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Indiana
                      </option>
                      <option value="IA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Iowa
                      </option>
                      <option value="KS"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Kansas
                      </option>
                      <option value="KY"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Kentucky
                      </option>
                      <option value="LA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Louisiana
                      </option>
                      <option value="ME"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Maine
                      </option>
                      <option value="MD"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>USA
                      </option>
                      <option value="MA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Massachusetts
                      </option>
                      <option value="MI"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Michigan
                      </option>
                      <option value="MN"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Minnesota
                      </option>
                      <option value="MS"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Mississippi
                      </option>
                      <option value="MO"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Missouri
                      </option>
                      <option value="MT"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Montana
                      </option>
                      <option value="NE"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Nebraska
                      </option>
                      <option value="NV"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Nevada
                      </option>
                      <option value="NH"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>New Hampshire
                      </option>
                      <option value="NJ"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>New Jersey
                      </option>
                      <option value="NM"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>New Mexico
                      </option>
                      <option value="NY"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>New York
                      </option>
                      <option value="NC"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>North Carolina
                      </option>
                      <option value="ND"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>North Dakota
                      </option>
                      <option value="OH"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Ohio
                      </option>
                      <option value="OK"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Oklahoma
                      </option>
                      <option value="OR"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Oregon
                      </option>
                      <option value="PA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Pennsylvania
                      </option>
                      <option value="RI"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Rhode Island
                      </option>
                      <option value="SC"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>South Carolina
                      </option>
                      <option value="SD"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>South Dakota
                      </option>
                      <option value="TN"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Tennessee
                      </option>
                      <option value="TX"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Texas
                      </option>
                      <option value="UT"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Utah
                      </option>
                      <option value="VT"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Vermont
                      </option>
                      <option value="VA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Virginia
                      </option>
                      <option value="WA"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Washington
                      </option>
                      <option value="WV"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>West Virginia
                      </option>
                      <option value="WI"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Wisconsin
                      </option>
                      <option value="WY"
                        <? if($varState=="Yes") echo(" selected=\"selected\"");?>>Wyoming
                      </option>
                    </select>
                  </p>
                  <p>
                    <label for='formZip'>Zip
                    </label>
                    <br/>
                    <input type="text" name="formZip" maxlength="5" value="<?=$varName;?>" />
                  </p>
                  <p>
                    <label for="for2" 'formCountry'>Country
                    </label>
                    <select name="formCountry">
                      <option value="">Select...
                      </option>
                      <option value="USA"
                              <? if($varCountry=="Yes") echo(" selected=\"selected\"");?>>USA
                      </option>
                    <option value="Canada"
                            <? if($varCountry=="No") echo(" selected=\"selected\"");?>>Canada
                  </option>
                  </select>
                  <br />
                  <br />
                  <label for='formEmail'>Email Address
                  </label>
                  <br/>
                  <input type="text" name="formEmail" maxlength="30" value="<?=$varName;?>" />
                  <br />
                  <br />
                  <label for="formComments">Comments (120 Char. Max)
                  </label>
                  <textarea name="formComments"  width="200" cols="30" rows="6" maxlength="120" id="textarea2">
                  </textarea>
                  <br />
                  <br />
                  <img src="/captcha_code_file.php?rand=<?php echo rand(); ?>"
                       id="captchaimg" >
                  <br />
                  <label for="message">Enter the code above here :
                  </label>
                  <input id="6_letters_code" name="6_letters_code" type="text">
                  <br />
                  </p>
                  <p>
                    <input type="submit" name="formSubmit" value="Submit" />
                  </p>
                </div>
              </td>
            </tr>
            <tr>
              <td valign="top">
                <input type="radio" name="formSubscribe" id="radio4" value="remove">
              </td>
              <td valign="top">
                <span class="subtext">No, remove me from the Arrow/Linear Technology catalog mailing list
                </span> 
                <br />
                <br />        
                <span class="subtext-2">
                  <i>Please fill out the form to the right so we can remove your name</i>
                </span> 
                <img src="/linear-catalog.png"/>
              </td>
            </tr>
          </form>
        </table>
        <br />
        <br />
      </div>
      <br />
      <br />
      <div class="footer" align="center">
        <span class="footertext">Any questions, email info@fwgprinting.com</span>
      </div>
    </div>
  </body>
</html>