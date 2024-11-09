#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

struct Point {
    double x, y;
};

Point basePoint;

Point findBasePoint(std::vector<Point> &points) {
    Point base = points[0];
    for (const auto &point : points) {
        if (point.y < base.y || (point.y == base.y && point.x < base.x)) {
            base = point;
        }
    }
    return base;
}

int calculateOrientation(Point p, Point q, Point r) {
    double value = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (value == 0) return 0;
    return (value > 0) ? 1 : 2;
}

bool compareByAngle(const Point &a, const Point &b) {
    int orientation = calculateOrientation(basePoint, a, b);
    if (orientation == 0) {
        return (basePoint.x - a.x) * (basePoint.x - a.x) + (basePoint.y - a.y) * (basePoint.y - a.y) <
               (basePoint.x - b.x) * (basePoint.x - b.x) + (basePoint.y - b.y) * (basePoint.y - b.y);
    }
    return orientation == 2;
}

std::vector<Point> grahamScan(std::vector<Point> &points) {
    int totalPoints = points.size();
    if (totalPoints < 3) return {};

    basePoint = findBasePoint(points);
    std::sort(points.begin(), points.end(), compareByAngle);

    std::vector<Point> convexHull = {points[0], points[1], points[2]};
    for (int i = 3; i < totalPoints; i++) {
        while (convexHull.size() > 1 && calculateOrientation(convexHull[convexHull.size() - 2], convexHull.back(), points[i]) != 2) {
            convexHull.pop_back();
        }
        convexHull.push_back(points[i]);
    }
    return convexHull;
}

std::vector<Point> loadPoints(const std::string &fileName) {
    std::ifstream file(fileName);
    std::vector<Point> points;
    double x, y;
    char comma;
    while (file >> x >> comma >> y) {
        points.push_back({x, y});
    }
    return points;
}

void saveConvexHull(const std::vector<Point> &convexHull, const std::string &fileName) {
    std::ofstream file(fileName);
    for (auto it = convexHull.rbegin(); it != convexHull.rend(); ++it) {
        file << it->x << "," << it->y << "\n";
    }
}

int main(int argc, char *argv[]) {
    std::string inputFile = argv[1];
    auto points = loadPoints(inputFile);
    auto convexHull = grahamScan(points);
    saveConvexHull(convexHull, "convexo.txt");

    return 0;
}
