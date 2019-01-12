<template>
  <div class="signup">
    <div class="signup__form">
      <input type="text" placeholder="Логин">
      <input type="password" class="pass" placeholder="Пароль">
      <input type="password" class="rep_pass" placeholder="Повторить пароль">
      <input type="email" class="email" placeholder="E-mail">
      <input type="submit" class="button button__submit" value="Зарегестрироваться">
    </div>
  </div>
</template>

<style scoped lang="scss">
  .signup{
    background: white;
    margin: 15% auto;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
    padding: 60px;
    width: 340px;
    border-radius: 50px;

    &__form {

    input {
      font-family: 'Cormorant Unicase';
      font-weight: 400;
      display: block;
      width: 90%;
      font-size: 1.3rem;
      padding: 7px 5%;
      border: 1px solid #e2e2e2;

      &.pass, &.rep_pass, &.email {
          color: #4b4b4b;
          margin: 20px 0;
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
      }
    }
  }
}
</style>