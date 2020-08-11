import React from 'react'
import '../../static/register.css'
import bg from'../../static/img/bg2.svg'

export default () => {
    return (
        <div class="container">
            <div class="company-name">
                <h2>Caption Gram</h2>
            </div>
            <div class="home-wrapper">
                <div class="img">
                    <img src={bg} alt="background"/>
                </div>
                <div class="form-wrapper">
                    <div class="login-info">
                        <p class="msg1">You're New Here!</p>
                        <p class="msg2">Let's get started on the process of getting a digital Address.</p>
                    </div>
                    <form>

                        <div class="input-container border-top">
                            <label for="first_name">First Name</label>
                            <input required class="input-field" type="text" placeholder="Enter Your First Name" name="first_name" required />
                        </div>
                        <div class="input-container border-bottom">
                            <label for="last_name">Last Name</label>
                            <input required class="input-field" type="text" placeholder="Enter Your Last Name" name="last_name" />
                        </div>

                        <div class="input-container border-full">
                            <label for="email">Email</label>
                            <input required class="input-field" type="email" placeholder="Enter Your Email" name="email" />
                        </div>

                        <div class="input-container border-full input-mobile">
                            <label for="number">Mobile Number</label>
                            <input required class="input-field" type="tel" pattern="[+]{1}[0-9]{11,14}" placeholder="eg: 772123456" name="number" />
                        </div>

                        <p class="msg-phone">You will receive a one-time passcode via SMS to verify the phone number</p>

                        <div class="input-container border-full">
                            <label for="password">password</label>
                            <input required class="input-field" type="password" placeholder="Enter Your Desired Password" name="password" />
                        </div>



                        <div class="two_row">
                            <button class="login">Sign Up</button>
                        </div>
                        <p class="msg-login">Have an account already? <a href="#">Login</a></p>

                    </form>
                </div>
            </div>
        </div>
    )
}