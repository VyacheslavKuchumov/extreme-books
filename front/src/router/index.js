import { createRouter, createWebHistory } from "vue-router";
import instance from "@/middlewares";


import HomeView from "@/views/HomeView.vue";
import Register from "@/views/Auth/Register.vue";
import Login from "@/views/Auth/Login.vue";
import AdminBooks from "@/views/Admin/AdminBooksView.vue";
import AdminQuizzes from "@/views/Admin/AdminQuizzesView.vue";
import AdminEvents from "@/views/Admin/AdminEventsView.vue";



const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: { auth: true },
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/admin/books",
    name: "admin-books",
    component: AdminBooks,
    meta: { auth: true },
  },
  {
    path: "/admin/quizzes",
    name: "admin-quizzes",
    component: AdminQuizzes,
    meta: { auth: true },
  },
  {
    path: "/admin/events",
    name: "admin-events",
    component: AdminEvents,
    meta: { auth: true },
  },

  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  try {
    const requireAuth = to.matched.some((record) => record?.meta.auth);
    if (requireAuth) {
      const uid = localStorage.getItem("uid");
      const response = await instance.get(`/api/users/${uid}`);
      if (response.status == 200) {
        return next();
      } else if (response.status == 403) {
        return next("/login");
      }
    }
    return next();
  } catch (error) {
    return next("/login");
  }
});

export default router;
