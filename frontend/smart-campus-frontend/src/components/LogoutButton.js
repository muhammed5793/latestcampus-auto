function LogoutButton() {
  const logout = () => {
    localStorage.clear();
    window.location.href = "/";
  };

  return <button onClick={logout}>Logout</button>;
}

export default LogoutButton;
