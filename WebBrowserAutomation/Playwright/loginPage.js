class LoginPage{
    constructor(page){
        this.page = page;
        this.usernameField = '#username';
        this.passwordField = '#password';
        this.loginButton = '#login > button'
    }

    async navigate(){
        await this.page.goto('https://the-internet.herokuapp.com/login');
    }

    async login(username, password){
        await this.page.fill(this.usernameField, username);
        await this.page.fill(this.passwordField, password);
        await this.page.click(this.loginButton);
    }
}

module.exports = LoginPage;