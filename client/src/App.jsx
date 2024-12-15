import { AppBar, Toolbar, Typography, Box, Grid, Paper } from "@mui/material";
import CandidateManagement from "./pages/CandidateManagement";
import JobManagement from "./pages/JobManagement";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
function App() {
  return (
    <Box sx={{ flexGrow: 1, height: "100vh" }}>
      {/* Header */}
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            My Application
          </Typography>
        </Toolbar>
      </AppBar>

      {/* Content */}
      <Box sx={{ padding: 2, height: "calc(100vh - 64px)" }}>
        <Grid container spacing={2} sx={{ height: "100%" }}>
          <Grid item xs={6}>
            <Paper
              sx={{
                height: "100%",
                overflowY: "auto",
              }}
            >
              <Box>
                <JobManagement />
              </Box>
            </Paper>
          </Grid>

          <Grid item xs={6}>
            <Paper
              sx={{
                height: "100%",
                overflowY: "auto",
              }}
            >
              <Box>
                <CandidateManagement />
              </Box>
            </Paper>
          </Grid>
        </Grid>
      </Box>
      <ToastContainer
        position="top-right"
        autoClose={1000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
    </Box>
  );
}

export default App;
