// src/pages/CandidateManagement.jsx
import { useState } from 'react';
import { Button, Typography, Box, AppBar, Toolbar, Dialog, DialogActions, DialogContent, DialogTitle, CircularProgress } from '@mui/material';
import ApiCandidateManagement from '../utils/api/candidate_managemet';
import CandidateList from '../components/CandidateList';
import UploadCV from '../components/UploadCV';
import DetailDialog from '../components/DetailDialog';
import { toast } from 'react-toastify'; // Thêm import Toastify

function CandidateManagement() {
  const [pdfFile, setPdfFile] = useState(null);
  const [candidates, setCandidates] = useState([]);
  const [candidateDetails, setCandidateDetails] = useState(null);
  const [openDialog, setOpenDialog] = useState(false); // Dialog upload file
  const [openUploadDialog, setOpenUploadDialog] = useState(false); // Dialog cho màn hình upload file

  // Hàm gọi API để thêm ứng viên mới (thay vì gửi PDF)
  const handleAddCandidate = async () => {
    if (!pdfFile) {
      toast.error('Please upload a PDF file first.'); // Hiển thị thông báo lỗi
      return;
    }

    try {
      const formData = new FormData();
      formData.append('file', pdfFile);
      const response = await ApiCandidateManagement.postExtractCVInfor(formData); // Thêm ứng viên mới
      if (!response.success) {
        toast.error(response.message); // Hiển thị thông báo lỗi
        return;
      }
      setPdfFile(null); // Reset file sau khi thêm
      setCandidates([...candidates, response.data]); // Cập nhật danh sách ứng viên
      setOpenUploadDialog(false); // Đóng dialog upload file sau khi thêm
    } catch (error) {
      console.error(error);
      toast.error('Failed to add candidate'); // Hiển thị thông báo lỗi
    }
  };

  // Hàm gọi API để lấy tất cả candidates
  const handleGetAllCandidates = async () => {
    try {
      const response = await ApiCandidateManagement.getAllCandidates();
      setCandidates(response.data);
      toast.success('Candidates retrieved successfully'); // Hiển thị thông báo thành công
    } catch (error) {
      console.error(error);
      toast.error('Failed to get all candidates'); // Hiển thị thông báo lỗi
    }
  };

  // Hàm gọi API để lấy chi tiết ứng viên theo id
  const handleGetCandidateDetails = async (id) => {
    try {
      const response = await ApiCandidateManagement.getCandidateById(id);
      setCandidateDetails(response.data);
      setOpenDialog(true);
      toast.success('Candidate details retrieved successfully'); // Hiển thị thông báo thành công
    } catch (error) {
      console.error(error);
      toast.error('Failed to get candidate details'); // Hiển thị thông báo lỗi
    }
  };

  // Hàm xóa ứng viên
  const handleDeleteCandidate = async (id) => {
    try {
      await ApiCandidateManagement.deleteCandidate(id);
      setCandidates(candidates.filter(candidate => candidate._id !== id)); 
      toast.success('Candidate deleted successfully'); // Hiển thị thông báo thành công
    } catch (error) {
      console.error(error);
      toast.error('Failed to delete candidate'); // Hiển thị thông báo lỗi
    }
  };

  // Hàm đóng dialog upload file
  const handleCloseUploadDialog = () => {
    setOpenUploadDialog(false);
  };

  return (
    <Box sx={{ padding: '20px' }}>
      {/* Thanh Header */}
      <AppBar position="sticky">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Candidate Management
          </Typography>
          <Button variant="contained" color="secondary" onClick={() => setOpenUploadDialog(true)}>
            Add Candidate
          </Button>
          <Button variant="contained" color="success" onClick={handleGetAllCandidates} sx={{ marginLeft: '10px' }}>
            Get All Candidates
          </Button>
        </Toolbar>
      </AppBar>

      {/* Hiển thị danh sách candidates dưới dạng các card */}
      <CandidateList
        candidates={candidates}
        onViewDetails={handleGetCandidateDetails}
        onDelete={handleDeleteCandidate}
      />

      {/* Popup Dialog hiển thị chi tiết ứng viên */}
      {candidateDetails ? (<DetailDialog
        open={openDialog}
        onClose={() => setOpenDialog(false)}
        candidateDetails={candidateDetails}
        />
      ):(
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <CircularProgress />
        </div>
        )
      }

      {/* Dialog upload file PDF để thêm ứng viên */}
      <Dialog open={openUploadDialog} onClose={handleCloseUploadDialog}>
        <DialogTitle>Add Candidate</DialogTitle>
        <DialogContent>
          <UploadCV onUpload={setPdfFile} />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseUploadDialog} color="primary">
            Cancel
          </Button>
          <Button onClick={handleAddCandidate} color="primary" variant="contained">
            Add Candidate
          </Button>
        </DialogActions>
      </Dialog>

    </Box>
  );
}

export default CandidateManagement;
