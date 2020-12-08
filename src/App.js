import React from 'react';import { HashRouter as Router, Route, Switch } from "react-router-dom";import HomeFeed from './homeFeed';import Login from './login';import Signup from './signup';import Profile from './profile';import './static/App.css';import Header from './header';import { useGlobalState } from './header';import { getCookie } from './authentication/getCookie';function App() {  const [isLogin, setIsLogin] = useGlobalState('isLogin');  if(getCookie('user')){    setIsLogin(true);  }  return (    <div className="App">      <Router>      	<Header />    		<Switch>    			<Route exact path="/" component={HomeFeed} />    			<Route exact path="/login" component={Login} />          <Route exact path="/account/signup" component={Signup} />          <Route exact path="/account/profile" component={Profile} />    		</Switch>    	</Router>    </div>  );}export default App;