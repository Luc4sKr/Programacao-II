const express = require("express");

const router = express.Router();

const tasksController = require("./controllers/tasksController");
const taskMiddleware = require("./middlewares/tasksMiddleware");

router.get("/tasks", tasksController.getAll);
router.post("/tasks", taskMiddleware.validateBody, tasksController.createTask);

module.exports = router;