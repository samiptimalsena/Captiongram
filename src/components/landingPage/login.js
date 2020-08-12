import React from 'react'
import '../../static/login.css'
import bg from '../../static/img/bg2.svg'
import { Link } from 'react-router-dom'
import { handleGoogleLogin } from '../../utils/firebase_login'

export default () => {
	return (
		<div class="container">
			<div class="company-name">
				<h2>Caption Gram</h2>
			</div>
			<div class="home-wrapper">
				<div class="img">
					<img src={bg} alt="background" />
				</div>
				<div class="form-wrapper">
					<div class="login-info">
						<p class="msg1">Welcome back :)</p>
						<p class="msg2">To keep connected with us please login with your personal information, by email and password,</p>
					</div>
					<form>
						<div class="input-container border-top">
							<i class="fas fa-envelope icon" />
							<input class="input-field" type="text" placeholder="Email" name="email" />
						</div>
						<div class="input-container border-bottom">
							<i class="fas fa-lock icon"></i>
							<input class="input-field" type="password" placeholder="Password" name="email" />
						</div>
						<div class="two_opposite">
							<div class="">
								<input type="checkbox" class="checkbox-round" id="remember" name="remember" value="remember" />
								<label for="remember"> Remember me</label>
							</div>
							<div>
								Forget Password?
						</div>
						</div>
						<div class="two_row">
							<button class="login">Login</button>
							<Link to='/register'>
								<button class="register">Create account</button>
							</Link>
						</div>
						<p class="msg-google">Or you can join with</p>

						<div>

							<div class="google-button" onClick={handleGoogleLogin}>
							</div>

						</div>

					</form>
				</div>
			</div>
		</div>
	)
}