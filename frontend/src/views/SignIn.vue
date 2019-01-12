<template>
    <div class="signin">
			<div class="signin__form">
				<input type="text" name="email" class="email" placeholder="e-mail">
				<input type="password" name="password" class="password"  placeholder="пароль">
				<input type="submit" class="button button__submit" v-on:click="login" value="Войти">
        <router-link to="/signin/signup">
         <input type="submit" class="button button__reg" value="Регистрация">
        </router-link>
			</div>
	</div>
</template>

<script>
export default {
  methods: {
    login: function(){
      this.$store.dispatch('login', {email: 'test@test.ru', password: '123456'});
    },
  }
}
</script>

<style scoped lang="scss">
  .signin {
    background: white;
    margin: 5% auto;
    box-shadow: 0 0 70px 0 rgba(0, 0, 0, 0.7), 0 5px 20px 0 rgba(0, 0, 0, 0.5);
    padding: 60px;
    width: 340px;
    border-radius: 10px;

    &__form {

      input{
        font-family: 'Cormorant Unicase';
        font-weight: 400;
        display: block;
        width: 90%;
        font-size: 1.3rem;
        padding: 7px 5%;
        border: 1px solid #e2e2e2;
        font-weight: 400;

        &.email, &.password {
          color: #4b4b4b;
          margin: 25px 0;
        }

        &.button {
          width: 100%;
          margin: 15px 0;
          font-size: 1.2rem;
          color: white;
          padding: 11px 0;
          text-align: center;

          &__submit {
            background: linear-gradient(120deg, rgb(12, 151, 175), rgb(12, 175, 175));


            &:hover {
              cursor: pointer;
              background: #007175;
            }
          }

          &__reg {
            background: linear-gradient(120deg, rgb(219, 216, 8), rgb(224, 174, 9));
            color: black;

            &:hover {
              cursor: pointer;
              background: #f5e507;
            }
          }
        }
      }
    }
  }

</style>