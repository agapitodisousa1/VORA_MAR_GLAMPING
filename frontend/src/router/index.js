import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/public/HomeView.vue";
import LoginView from "../views/public/LoginView.vue";
import AlojamientosView from "../views/public/AlojamientosView.vue";
import DashboardView from "../views/admin/DashboardView.vue";
import ReservasAdminView from "../views/admin/ReservasAdminView.vue";
import ReservasView from "@/views/public/ReservasView.vue";
import RegisterView from "@/views/public/RegisterView.vue";
import InstalacionesView from "@/views/public/InstalacionesView.vue";
import MisReservasView from "@/views/public/MisReservasView.vue";
import NotFoundView from "../views/public/NotFoundView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView
  },
  {
    path: "/mis-reservas",
    name: "mis-reservas",
    component: MisReservasView
  },

  {
    path: "/login",
    name: "login",
    component: LoginView
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView
  },
  {
    path: "/instalaciones",
    name: "instalaciones",
    component: InstalacionesView
  },
  {
    path: "/alojamientos",
    name: "alojamientos",
    component: AlojamientosView
  },
  {
    path: "/reservas",
    name: "reservas",
    component: ReservasView
  },
  {
    path: "/admin/dashboard",
    name: "dashboard",
    component: DashboardView,
    meta: {
      requiresAuth: true,
      adminOnly: true 
    }
  },

  {
    path: "/admin/reservas",
    name: "reservas-admin",
    component: ReservasAdminView,
    meta: {
      requiresAuth: true,
      adminOnly: true
    }
  },
  {
    path: "/:pathMatch(.*)*",
    name: "404",
    component: NotFoundView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {

  const token = localStorage.getItem("token")
  const user = JSON.parse(localStorage.getItem("user"))
  if (to.meta.requiresAuth && !token) {
    return next("/login");
  }
  if (to.meta.adminOnly && user?.rol !== "admin") {
    return next("/")
  }
  next();
});

export default router;