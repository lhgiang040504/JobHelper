import axios from "axios";

const instance = axios.create({
  // baseURL: "https://quanlithuvien.onrender.com/api/",
  baseURL: "http://127.0.0.1:8000/",
  withCredentials: true
});

// Thêm một bộ đón chặn request
instance.interceptors.request.use(
  function (config) {
    // Làm gì đó trước khi request được gửi đi
    let localStorageData = window.localStorage.getItem(
      "persist:qltv/user"
    );
    if (localStorageData && typeof localStorageData === "string") {

      localStorageData = JSON.parse(localStorageData);
      const accessToken = JSON.parse(localStorageData?.token);
      config.headers = {
        Authorization: `Bearer ${accessToken}`,
      };
      return config;
    } else return config;
  },
  function (error) {
    // Làm gì đó khi lỗi
    return Promise.reject(error);
  }
);

// Thêm một bộ đón chặn response
instance.interceptors.response.use(
  function (response) {
    // Bất kì mã trạng thái nào nằm trong tầm 2xx đều khiến hàm này được trigger
    // Làm gì đó với dữ liệu response
    return response.data;
  },
  function (error) {
    if (error.response) {
      if (error.response.status === 401) {
        window.localStorage.removeItem("persist:qltv/user");
        window.location.reload();
      }
      return error.response.data;
    }
  }
);

export default instance;
