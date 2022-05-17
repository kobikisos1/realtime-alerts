real_time_email_template_head = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
<head style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
<meta name="viewport" content="width=device-width" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" />
<link href="http://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet" type="text/css" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
<style style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
* {
 margin:0;
padding:0;
}

@font-face {
  font-family: 'Quicksand';
  font-style: normal;
  font-weight: 500;
  src: url(https://fonts.gstatic.com/s/quicksand/v22/6xK-dSZaM9iE8KbpRA_LJ3z8mH9BOJvgkP8o58a-xDwxUD2GFw.woff) format('woff');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

* { font-family: "Quicksand", "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; }

img {
	max-width: 100%;
}
body {
	-webkit-font-smoothing:antialiased;
	-webkit-text-size-adjust:none;
	width: 100%!important;
	height: 100%;
}

table.head-wrap { width: 100%;}

.header.container table td.logo { padding: 15px; }
.header.container table td.label { padding: 15px; padding-left:0px;}

table.body-wrap { width: 100%;}


h1 small, h2 small, h3 small, h3 small, h3 small, h6 small { color: #000000; line-height: 0; text-transform: none; }

h1 { font-weight:600; font-size: 28px;}
h2 { font-weight:600; font-size: 22px;}
h3 { font-weight:600; font-size: 16px;}

.container {
display:block!important;
max-width:600px!important;
 margin:0 auto!important; 
clear:both!important;
}

.content {
padding:10px;
max-width:600px;
 margin:0 auto;
display:block;
}

.small_table{
width:220px;
 margin-left: 10px;
}

.content table { width: 100%; }

.vertical_line_container{
 margin-right: 20px;
 margin-left: 20px;
padding-top: 6px;
height: 120px;
}

.vertical_line{
width: 6px;
height: 112px;
border-radius: 30px;
background: #7b00ffff;
}

.blue_button{
 margin:0 auto;
background: #00aaffff;
color: white;
width: 160px;
padding: 15px;
text-align: center;
font-weight: 600;
border-radius: 5px;
}

</style>
</head>
'''

real_time_email_template_body = '''
<body bgcolor="#FFFFFF" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;width:100%!important;height:100%;" >
<table class="head-wrap" bgcolor="#000000" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
	<tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
		<td class="header container" align="" style="padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;display:block!important;max-width:600px!important;margin-top:0 !important;margin-bottom:0 !important;margin-right:auto !important;margin-left:auto !important;clear:both!important;" >
			<div class="content" style="font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;padding-top:10px;padding-bottom:10px;padding-right:10px;padding-left:10px;max-width:600px;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;display:block;" >
				<table bgcolor="#000000" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
					<tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
						<td align="center" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" ><img src="https://assetsfordemo.s3-eu-west-1.amazonaws.com/daily_emails/sensi_logo_slogan.png" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;max-width:100%;" /></td>
					</tr>
					<tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
						<td align="right" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" ><img src="https://assetsfordemo.s3-eu-west-1.amazonaws.com/daily_emails/sensi_logo_dots_row.png" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;max-width:100%;" /></td>
					</tr>
				</table>
			</div>
		</td>
	</tr>
</table>
<table class="body-wrap" bgcolor="" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
	<tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
		<td class="container" align="" bgcolor="#FFFFFF" style="padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;display:block!important;max-width:600px!important;margin-top:0 !important;margin-bottom:0 !important;margin-right:auto !important;margin-left:auto !important;clear:both!important;" >
			<div class="content" style="font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;padding-top:10px;padding-bottom:10px;padding-right:10px;padding-left:10px;max-width:600px;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;display:block;" >
				<table style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
					<tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
						<td style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
							<h4 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:24px;" >According to the data analyzed by 
							    <a href="https://app.sensi.ai" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;text-decoration:none;cursor:pointer;display:inline;" >Sensi.ai</a>,<br>
							    you have a high-level alert! <br>We recommend you take a look.
							</h4>
							
						</td>
					</tr>
				</table>
			</div>
            <div class="content" style="font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;padding-top:10px;padding-bottom:10px;padding-right:10px;padding-left:10px;max-width:600px;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;display:block;" >
                <table style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
                    <tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                        <td align="left" width="80%" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                            <table style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
                                <tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:top;" >
                                    <td align="left" valign="middle" width="100%" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                                        <table style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
                                          <tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                                            <td valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:32px;" >
                                                <img  src="https://assetsfordemo.s3-eu-west-1.amazonaws.com/assign_email/assign_purple_bell.png" style="margin-top:0;margin-bottom:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;margin-right:25px;max-width:100%;" />
                                            </td>
                                             <td valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;" >
                                                <h2 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;display:inline;padding-left:4px;font-weight:600;font-size:22px;" >Alert Details:</h2>
                                            </td>
                                          </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </div>
            <div class="content" style="font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;padding-top:10px;padding-bottom:10px;padding-right:10px;padding-left:10px;max-width:400px;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;display:block;" >                
                <table style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
                    <tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:18px;" >
                            <img  src="https://assetsfordemo.s3-eu-west-1.amazonaws.com/assign_email/assign_home.png" style="margin-top:0;margin-bottom:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;margin-right:25px;max-width:100%;" />
                        </td>
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:50px;" >
                            <h3 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:16px;" >Home:</h3>
                        </td>
                        <td rowspan="3" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:10px;" >
                            <div class="vertical_line_container" style="margin-top:0;margin-bottom:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;margin-right:20px;margin-left:20px;padding-top:6px;height:120px;" >
                                <div class="vertical_line" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;background-attachment:scroll;width:6px;height:112px;border-radius:30px;background-color:#7b00ffff;background-image:none;background-repeat:repeat;background-position:top left;" ></div>
                            </div>
                        </td>
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:50px;" >
                            <h3 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:16px;" >{unit}</h3>
                        </td>
                    </tr>
                    <tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:18px;" >
                            <img  src="https://assetsfordemo.s3-eu-west-1.amazonaws.com/assign_email/assign_label.png" style="margin-top:0;margin-bottom:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;margin-right:25px;max-width:100%;" />
                        </td>
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:50px;" >
                            <h3 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:16px;" >Label:</h3>
                        </td>
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:50px;" >
                            <h3 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:16px;" >{labels}</h3>
                        </td>
                    </tr>
                    <tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:18px;" >
                            <img  src="https://assetsfordemo.s3-eu-west-1.amazonaws.com/assign_email/assign_time.png" style="margin-top:0;margin-bottom:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;margin-right:25px;max-width:100%;" />
                        </td>
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:60px;" >
                            <h3 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:16px;" >Date & Time:</h3>
                        </td>
                        <td align="left" valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;width:100px;" >
                            <h3 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:16px;" > {time}</h3>
                        </td>
                    </tr>
                </table>
            </div>
			<div class="content" style="font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;padding-top:10px;padding-bottom:10px;padding-right:10px;padding-left:10px;max-width:600px;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;display:block;" >
				<table style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;width:100%;" >
					<tr style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
						<td style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;" >
							<div class="blue_button" style="font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;background-attachment:scroll;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;background-color:#00aaffff;background-image:none;background-repeat:repeat;background-position:top left;color:white;width:380px;padding-top:15px;padding-bottom:15px;padding-right:15px;padding-left:15px;text-align:center;font-weight:600;border-radius:5px;" >
                                <h2 style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;font-weight:600;font-size:22px;" >
                                    <a  href="https://app.sensi.ai" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;text-decoration:none;color:white;cursor:pointer;display:inline-block;" >
                                        View Alert
                                    </a>
                                </h2>
                            </div>
						</td>
                    </tr>
                    <tr>
						<td valign="middle" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;vertical-align:middle;" >
                            <br><br>
                            <p style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;font-family:'Quicksand', 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;display:inline;padding-left:4px;font-weight:600;font-size:16px;" >Note: This notification is sent to the agency’s contact list.</p>
                        </td>
					</tr>
				</table>
			</div>
		</td>
	</tr>
</table>
</body>
</html>
'''
