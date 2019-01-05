<template>
    <div class="main-signup">
		<div class="main-signup__head">
			<p>Sign Up</p>
		</div>
		<div class="main-signup__middle">
			<form>
				<input type="text" placeholder="Login">
				<input type="password" placeholder="Password">
                <input type="password" placeholder="Repeat Password">
                <input type="email" placeholder="E-mail">
				<input type="submit" value="Sign Up">
			</form>
		</div>
	</div>
</template>

<style scoped lang="scss">
.main-signup {
    width: 455px;
    height: 250px;
    margin: 20px auto;

    &__head {
        background: #000;
        border-bottom: 1px solid #2d2f32;
        border-radius: 10px 10px 0 0;
        padding: 6px 0;

        p {

        }
    }
    
}
.main-signup .main-signup__head {

}
.main-signup .main-signup__head p {
  color: #586069;
  text-align: left;
  font-size: 18px;
  padding-left: 25px;
}
.main-signup .main-signup__middle {
  background: #000;
  border-bottom: 1px solid #2d2f32;
  border-top: 1px solid #2d2f32;
  border-radius: 0 0 10px 10px;
}
.main-signup .main-signup__middle form {
  margin: 20px 0 20px 0;
}
.main-signup .main-signup__middle form input[type="text"], .main-signup .main-signup__middle form input[type="password"], .main-signup .main-signup__middle form input[type="password"], .main-signup .main-signup__middle form [type="email"], .main-signup .main-signup__middle form input[type="submit"] {
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
.main-signup .main-signup__middle form input[type="text"], .main-signin .main-signin__middle .middle__form input[type="password"], .main-signup .main-signup__middle form input[type="password"], .main-signup .main-signup__middle form [type="email"] {
  padding:15px 20px;
  width:81%;
}
.main-signup .main-signup__middle form input[type="password"], .main-signup .main-signup__middle form [type="email"] {
  border-top: 1px solid #acabab;
  border-radius: 0 0 5px 5px;
}
.main-signup .main-signup__middle form input[type="submit"] {
  background: #e6b333;
  border-radius: 5px;
  color: #f5f5f5;
  font-size: 18px;
  margin-top: 15px;
  cursor:pointer;
}
.main-signup .main-signup__middle form input[type="submit"]:active {
  background: #80d6f7;
}

</style>