import LoginButton from "./components/LoginButton";
import LogoutButton from "./components/LogoutButton";
import AuthHandler from "./components/AuthHandler";
import AccountCreation from "./components/AccountCreation";

function App() {
  return (
    <main>
      <LoginButton/>
      <LogoutButton/>
      <AuthHandler/>
      <AccountCreation/>
    </main>
  );
}

export default App;
