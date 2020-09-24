<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2009/11/20
            <br />
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          注册
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              用户名:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="username" v-model="username" />
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              真实姓名:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="name" v-model="real_name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              密码:
            </td>
            <td valign="middle" align="left">
              <input type="password" class="inputgri" name="pwd" v-model="password" />
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              确认密码:
            </td>
            <td valign="middle" align="left">
              <input type="password" class="inputgri" name="pwd" v-model="re_word"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              性别:
            </td>
            <td valign="middle" align="left">
              男
              <input type="radio" class="inputgri" name="sex" value="m" checked="checked"  @click="gender=0"/>
              女
              <input type="radio" class="inputgri" name="sex" value="f" @click="gender=1"/>
            </td>
          </tr>

        </table>
        <p>
           <el-button plain @click="submit">注册</el-button>
        </p>
      </div>
    </div>
    <div id="footer">
      <div id="footer_bg">
        ABC@126.com
      </div>
    </div>
  </div>
</template>

<script>
export default {
name: "register",
  data(){
    return{
      username:'',
      real_name:'',
      password:'',
      re_word:'',
      gender:0,
    }
  },

  methods:{
  register(){
    if (this.password!==this.re_word){
      this.$message.error('两次密码不一致');
      this.password='',
        this.re_pwd='',
      return
    }else if (this.password===this.re_word){
      this.$axios({
        url:'http://127.0.0.1:8000/api/users/',
        method:'post',
        data:{
          username:this.username,
          password:this.password,
          real_name:this.real_name,
          gender:this.gender,
          re_pwd:this.re_word,
        },
      }).then(response=>{

        if (response.data.message){
          this.$message({
            message:'注册成功',
            type:'success',
            duration:1000,
            showClose:true,
          });
          //跳转登录
          this.$message('注册成功');
          this.$router.push('/login')
        }
      }).catch(error=>{
        console.log(error.message);
        this.$message.error('用户名已存在或密码错误');
      })
    }

    }
}

}

</script>

<style scoped>

</style>
