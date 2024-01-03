import streamlit as st


def about_function():
    html_about_prog = """
        <body>
            <div style="background-color: rgb(0, 0, 0);border-radius: 20px;padding: 10px; border:2px solid #009fe8;"class="main-div>
                <div style="color:#009fe8; class="developers">
                    <h1 class="dev-by">Developed by : </h1> 
                    <ul style="font-size:20pt;padding-left:50px;">
                        <h3>Firas Daha</h3>
                        <h3>Ghasan Shakeeb</h3>
                        <h3>Ateeq Shwbas</h3>
                    </ul>
                </div>
            <hr>
                <div style="background-color: rgb(0, 0, 0); border:2px solid #009fe8; border-radius: 20px;padding: 20px;" class="prog-data">
                <h2>Email : firas.prog.it@gmail.com</h2>
                </div>           
            </div>
        </body>
    """
    css_about_prog = """
                body {
                    background-color: rgb(41, 50, 60);
                }
                .prog-data {
                    background-color: rgb(0, 0, 0);
                    border-radius: 20px;
                    padding: 20px;
                    margin-top: 30%;
                    color: rgb(248, 248, 255);
                    border: 3px solid rgb(246, 254, 255);
                    font-size:12px;
                }
                .main-div .developers {
                    background-color: rgb(0, 0, 0);
                    border-radius: 20px;
                    padding: 10px;
                    margin-top: 10%;
                    color: rgb(248, 248, 255);
                    border: 3px solid rgb(247, 254, 255);
                    font-size: 12px;
                }
                .main-div{
                    text-align: center;
                        font-size: 14px;
                        color: lightgrey;
                        font-family: 'Source Sans Pro', sans-serif;
                }
                .developers .dev-by{
                    margin-top: -1px;
                        margin: 0px 15px 0px 15px;
                        border-radius: 20px;
                        background-color: rgb(0, 96, 109);
                }  
    """
    st.markdown(html_about_prog, unsafe_allow_html=True)

    def local_css(css_about_prog):
        with open(css_about_prog) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # local_css("/css/about_prog.css")

    # st.title("hello in about page")
