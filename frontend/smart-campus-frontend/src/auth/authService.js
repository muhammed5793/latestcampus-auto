import api from "../api/axios";

export const login = async (username, password) => {
  try {
    const response = await api.post("auth/token/", {
      username,
      password,
    });

    localStorage.setItem("token", response.data.access);
    localStorage.setItem("role", response.data.role);

    return response.data;
  } catch (error) {
    throw new Error("Login failed");
  }
};
