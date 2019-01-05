<template>
    <div class="main-signin">
		<div class="main-signin__head">
			<p>Sign In</p>
		</div>
		<div class="main-signin__middle">
			<div class="middle__form">
				<input type="text" placeholder="Login">
				<input type="password" placeholder="Password">
				<input type="submit" value="Sign In">
			</div>
		</div>
	</div>
</template>

<style lang="css">
 .main-signin {
    width: 455px;
    height: 250px;
    margin: 20px auto;
 }
 .main-signin .main-signin__head {
  background: #000;
  border-bottom: 1px solid #2d2f32;
  border-radius: 10px 10px 0 0;
  padding: 6px 0;
}
.main-signin .main-signin__head p {
  color: #586069;
  text-align: left;
  font-size: 18px;
  padding-left: 25px;
}
.main-signin .main-signin__middle {
  background: #000;
  border-bottom: 1px solid #2d2f32;
  border-top: 1px solid #2d2f32;
  border-radius: 0 0 10px 10px;
}
.main-signin .main-signin__middle .middle__form {
  margin: 20px 0 20px 0;
}
.main-signin .main-signin__middle .middle__form ::-webkit-input-placeholder {
  color: #25262a;
}
.main-signin .main-signin__middle .middle__form input[type="text"], .main-signin .main-signin__middle .middle__form input[type="password"], .main-signin .main-signin__middle .middle__form input[type="submit"] {
  background: #f5f5f5;
  border-radius: 5px 5px 0 0;
  border: none;
  color: #25262a;
  display: block;
  margin: 0 20px;
  outline: none;
  padding: 15px 0;
  width: 90%;
}
.main-signin .main-signin__middle .middle__form input[type="text"], .main-signin .main-signin__middle .middle__form input[type="password"] {
  padding:15px 20px;
  width:81%;
}

.main-signin .main-signin__middle .middle__form input[type="password"] {
  border-top: 1px solid #acabab;
  border-radius: 0 0 5px 5px;
}
.main-signin .main-signin__middle .middle__form input[type="submit"] {
  background: #e6b333;
  border-radius: 5px;
  color: #f5f5f5;
  font-size: 18px;
  margin-top: 15px;
  cursor:pointer;
}
.main-signin .main-signin__middle .middle__form input[type="submit"]:active {
  background: #80d6f7;
}

</style>