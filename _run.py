from viewer import DataViewer
import sys

if __name__ == '__main__':
    app = DataViewer(sys.argv)

    sys.exit(app.exec_())
